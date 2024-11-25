import { Component, OnInit, ViewChild } from '@angular/core';
import { MenuController } from '@ionic/angular';
import { IonModal } from '@ionic/angular';
import { Item } from '../types/type'
import { Modalidade } from '../types/modalidade';
import { Localidade } from '../types/localidade'
import { ApiService } from '../api.service';
import { ApiCadastroService } from './api-cadastro.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.page.html',
  styleUrls: ['./cadastro.page.scss'],
})
export class CadastroPage implements OnInit {
  @ViewChild('modal_modalidades', { static: true }) modal_modalidades!: IonModal;
  @ViewChild('modal_localidade', { static: true }) modal_localidade!: IonModal;
  
  dados_validos = false;
  mensagem_erro: string = "Credenciais inválidas.";

  modalidades_para_escolha: Item[] = [];
  modalidades_escolhidas: string[] = [];
  
  locais_para_escolha: Item[] = [];

  username: string = "";
  password: string = "";
  grupo: string = "jogador";

  residencia_label = "Selecionar localidade";
  
  usuario: {
    nome_completo: string;
    email: string;
    residencia: number | undefined;
    data_nascimento: string;
    partidas_concluidas: number;
    contato: string;
  } = {
    nome_completo: "",
    email: "",
    residencia: undefined,
    data_nascimento: "",
    partidas_concluidas: 0,
    contato: ""
  };
  
  constructor(private menuCtrl: MenuController, private ApiService: ApiService, private ApiCadastroService: ApiCadastroService, private roteante: Router) { }

   ngOnInit() {
    this.menuCtrl.enable(false);
    this.puxar_modalidades();
    this.puxar_localidades();
  }

  ionViewWillLeave() {
    this.menuCtrl.enable(true);
  }

  cadastro()
  {
    const ta_certo = this.username && this.password && this.grupo && 
    this.usuario.nome_completo && this.usuario.email && this.usuario.residencia != null && 
    this.usuario.data_nascimento && this.usuario.contato && this.modalidades_escolhidas.length > 0;
    
    if (ta_certo)
      {
        const dados = 
        {
          username: this.username,
          password: this.password,
          grupo: this.grupo,
          usuario: this.usuario,
          modalidades: this.modalidades_escolhidas
        };
    
        console.log(dados);

        this.usuario.contato = this.limparTelefone(this.usuario.contato);

      if (this.usuario.contato.length === 11)
      {
        this.ApiCadastroService.cadastro(dados).subscribe(
          (response: any) => {
            console.log(response);
            localStorage.setItem('token', response.token);
            this.roteante.navigate(['/menu']);
    
          }, (error) => {
            console.log("erro: " + error);
            this.m_torrada(true, "Credenciais Inválidas.");
          })
      } else {
        // alert("O Numero de contato deve ter 11 caracteres.");
        this.m_torrada(true, "Número de contato inválido.");

      }
    } else {
      // alert("Preencha todos os campos.");
      this.m_torrada(true, "Preencha todos os campos.");

    }
  }


  modalidade_selecionadas(selecionadas: string[])
  {
    this.modalidades_escolhidas = selecionadas;
    console.log('Modalidades selecionadas:', this.modalidades_escolhidas);
    this.modal_modalidades.dismiss();
  }

  localidade_selecionada(localidade: number)
  {
    this.usuario.residencia = localidade;
    console.log('Localidade Escolhida (cadastro.ts):', this.usuario.residencia);
    this.modal_localidade.dismiss();
  }

  puxar_modalidades()
  {
    this.ApiService.modalidades().subscribe({
      next: (data: Modalidade[]) => {
        data.forEach((d=>{
          this.modalidades_para_escolha.push({
            id: d.id,
            value: d.modalidade
          });
        }))
      }, error: (err)=> {
        console.error("Erro em carregar modalidades: " + err);
      }
    })
  }

  puxar_localidades() 
  {
    this.ApiService.locais().subscribe({
      next: (data: Localidade[]) => {
          data.forEach((d) => {
              this.locais_para_escolha.push({
                  id: d.id,
                  value: `${d.cidade}-${d.estado}`
              });
          });
        },
        error: (err) => {
            console.error("Erro em carregar localidades:", err);
        }
    })
  }

  m_torrada(situacao: boolean, mensagem: string)
  {
    this.dados_validos = situacao;

    if (situacao)
    {
      this.mensagem_erro = mensagem;
    }
  }

  limparTelefone(telefone: string): string {
    return telefone.replace(/[^\d]/g, '');
  }
}
