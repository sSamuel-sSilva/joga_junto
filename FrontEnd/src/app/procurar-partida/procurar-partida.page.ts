import { Component, OnInit, ViewChild } from '@angular/core';
import { ApiProcurarPartidaService } from './api-procurar-partida.service';
import { Partida } from '../types/partida';
import { Modalidade } from '../types/modalidade';
import { Item } from '../types/type';
import { ApiService } from '../api.service';
import { IonModal, MenuController } from '@ionic/angular';
import { Location } from '@angular/common';
import { Router } from '@angular/router';
 

@Component({
  selector: 'app-procurar-partida',
  templateUrl: './procurar-partida.page.html',
  styleUrls: ['./procurar-partida.page.scss'],
})
export class ProcurarPartidaPage implements OnInit {
  @ViewChild('modal_modalidade', { static: true }) modal_modalidade!: IonModal;
  @ViewChild('modal_ct_pol', { static: true }) modal_ct_pol!: IonModal;

  tem_partida: boolean = false;
  mensagem_torrada = "";

  modalidade: number = 0;
  ct_pol: number = 0;

  partidas: Partida[] = [];
  modalidades_escolha: Item[] = [];
  ctpols_escolha: Item[] = [];

  constructor(private local: Location, private menuCtrl: MenuController, private api: ApiProcurarPartidaService, private ApiService: ApiService, private roteante: Router) { }

  ngOnInit() {
    this.esta_logado();
    this.procurar_partida(0, 0);
    this.puxar_modalidades();
    this.puxar_ctpols_proximos();
  }

  ionViewWillEnter(): void 
  {
    this.esta_logado();
    this.procurar_partida(0, 0);
    this.puxar_modalidades();
    this.puxar_ctpols_proximos();
  }

  esta_logado()
  {
    const token = localStorage.getItem("token");
    console.log(token);
    if (!token)
    {
      this.roteante.navigate(['/login']);
    }
  }

  openMenu() {
    this.menuCtrl.open();
  }

  voltar(): void {
    this.local.back();
  }

  procurar_partida(modalidade: number, ctpol: number)
  {
    const token = localStorage.getItem('token');
    if (token != null)
    {
      this.api.procurar_partida(token, modalidade, ctpol).subscribe({
        next: (data: any)=> {
          console.log(data);
          if (data.Situação === "Sem partidas encontradas nesse momento.")
          {
            this.m_torrada(true, "Sem partidas encontradas nesse momento.");
          }

          if (data.Situação === "Sem partidas encontradas para essa filtragem.")
          {
            this.m_torrada(true, "Sem partidas encontradas para essa filtragem.");
          } 

          if (data.Situação === "Sem partidas encontradas na sua região.")
          {
            this.m_torrada(true, "Sem partidas encontradas na sua região.");
          } 
          
          if (data.length > 1)
          {
            data.forEach((d:any)=> {
              const [data_desformata, dia_escrito] = d.data.split(',');
              const data_formatada = this.formatarData(data_desformata);

              const data_completa = `${data_formatada}, ${dia_escrito}`;

              this.partidas.push({
                ct: d.ct,
                data: data_completa,
                fim: d.fim.slice(0, -3),
                inicio: d.inicio.slice(0, -3),
                lider: d.lider,
                modalidade: d.modalidade,
                residencia: d.residencia,
              })
           })
          }


        }, error(err) {
          console.error("Erro em buscar partidas: " + err);
        },
      })
    }
  }

  puxar_modalidades()
  {
    this.ApiService.modalidades().subscribe({
      next: (data: Modalidade[]) => {
        data.forEach((d=>{
          this.modalidades_escolha.push({
            id: d.id,
            value: d.modalidade
          });
        }))
        console.log(this.modalidades_escolha);
      }, error: (err)=> {
        console.error("Erro em carregar modalidades: " + err);
      }
    })
  }

  puxar_ctpols_proximos()
  {
    const token = localStorage.getItem('token');
    if (token != null)
    {
      this.api.ctpols_proximos(token).subscribe({
        next: (data: any) => {
          
          data.ctpol.forEach((d: any)=>{
            this.ctpols_escolha.push({
              id: d.id,
              value: d.nome
            })
          })

          console.log(this.ctpols_escolha);

        }, error: (err)=> {
          console.error("Erro em carregar ctpols_proximos:", err);
        }
      })
    } else {
      console.log("Token inexistente.");
    }
  }

  modalidade_selecionada(modalidade: number)
  {
    this.modalidade = modalidade;
    console.log('Modalidade escolhida (cadastro.ts):', this.modalidade);
    this.modal_modalidade.dismiss();
    this.procurar_partida(this.modalidade, this.ct_pol);
  }

  ct_pol_selecionado(ct_pol: number)
  {
    this.ct_pol = ct_pol;
    console.log('CT escolhido (cadastro.ts):', this.ct_pol);
    this.modal_ct_pol.dismiss();
    this.procurar_partida(this.modalidade, this.ct_pol);
  }

  m_torrada(situacao: boolean, mensagem: string)
  {
    this.tem_partida = situacao;

    if (situacao)
    {
      this.mensagem_torrada = mensagem;
    }
  }

  formatarData(data: string): string 
  {
    const [parteData] = data.split(',');
    const [ano, mes, dia] = parteData.split('-');
    return `${dia}/${mes}/${ano}`;
  }
}
