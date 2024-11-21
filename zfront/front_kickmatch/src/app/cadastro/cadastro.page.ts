import { Component, OnInit } from '@angular/core';
import { ApiCadastroService } from './api-cadastro.service'; 
import { ApiGeralService } from '../api-geral.service'; 
import { MenuController } from '@ionic/angular';
import { Local } from '../models/localidade.models'
import { Modalidade } from '../models/modalidade.models';
import { NavController } from '@ionic/angular';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.page.html',
  styleUrls: ['./cadastro.page.scss'],
})

export class CadastroPage implements OnInit {
  locais_escolha: Local[] = [];
  modalidades_escolha: Modalidade[] = [];

  username: string = "";
  password: string = "";
  grupo: string = "jogador";
  
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
  
  modalidades: number[] = [];

  constructor(private ApiCadastroService: ApiCadastroService, private ApiGeralService: ApiGeralService, private menuCtrl: MenuController, private navCtrl: NavController) { }

  ngOnInit() {
    this.menuCtrl.enable(false);
    this.carregar_locais();
    this.carregar_modalidades();
  }

  ionViewWillLeave() {
    this.menuCtrl.enable(true);
  }

  cadastro()
  {
    const ta_certo = this.username && this.password && this.grupo && 
    this.usuario.nome_completo && this.usuario.email && this.usuario.residencia != null && 
    this.usuario.data_nascimento && this.usuario.contato && this.modalidades.length > 0;
    
    if (ta_certo)
      {
        const dados = 
        {
          username: this.username,
          password: this.password,
          grupo: this.grupo,
          usuario: this.usuario,
          modalidades: this.modalidades
        };

      if (this.usuario.contato.length === 11)
      {
        this.ApiCadastroService.cadastro(dados).subscribe(
          (response: any) => {
            console.log(response);
            localStorage.setItem('token', response.token);
            this.navCtrl.navigateRoot('/menu');
    
          }, (error) => {
            console.log("erro: " + error);
            alert("Credenciais inválidas")
          })
      } else {
        alert("O Numero de contato deve ter 11 caracteres.");
      }
    } else {
      alert("Preencha todos os campos.");
    }
  }

  carregar_locais()
  {
    this.ApiGeralService.locais().subscribe({
      next: (data: Local[]) => {
        this.locais_escolha = data;
      },
      error: (err)=> {
        console.error("Erro em carregar locais: " + err);
      }
    })
  }

  carregar_modalidades()
  {
    this.ApiGeralService.modalidades().subscribe({
      next: (data: Modalidade[]) => {
        this.modalidades_escolha = data;
      }, error: (err)=> {
        console.error("Erro em careegar modalidades: " + err);
      }
    })
  }

  onRadioChange(event: any) {
    this.usuario.residencia = event.detail.value;
  }
}
