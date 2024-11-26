import { Component, OnInit } from '@angular/core';
import { IonRouterOutlet, MenuController, PopoverController } from '@ionic/angular';
import { ApiService } from './api.service';
import { Perfil } from '../types/perfil';
import { Router } from '@angular/router';
import { Location } from '@angular/common';


@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.page.html',
  styleUrls: ['./perfil.page.scss'],
})
export class PerfilPage implements OnInit {

  perfil: Perfil | undefined;
  modalidades: string[] = [];
  idade: number = 0;

  alertButtons = [
    {
      text: 'Cancelar',
      role: 'cancel',
      handler: () => {
        console.log('cancelo');
      },
    },
    {
      text: 'Confirmar',
      role: 'confirm',
      handler: () => {
        console.log('confirmo');
      },
    },
  ];

  constructor(private ApiService: ApiService, private menuCtrl: MenuController, private roteante: Router, private popOver: PopoverController, private local: Location) { }

  ngOnInit()
  {
    this.esta_logado();
    this.puxar_perfil();
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

  puxar_perfil()
  {
    const token = localStorage.getItem('token');
    if (token != null)
    {
      this.ApiService.perfil(token).subscribe({
        next: (data: any) => {
          data.usuario.contato = this.formatarTelefone(data.usuario.contato);
          this.idade = this.calcularIdade(data.usuario.data_nascimento);
          this.perfil = data.usuario;


          data.modalidades.forEach((d: string)=>{
            this.modalidades.push(d);
          })

          console.log(this.perfil);
          console.log(this.modalidades);
        }, error: (err)=>{
          console.error("Erro em carregar dados do perfil:", err);
        }
      })
    } else {
      console.log("Token inexistente.");
    }
  }

  openMenu() {
    this.menuCtrl.open();
  }

  formatarTelefone(numero: string) 
  {
    if (numero.length === 11) {
        return numero.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
    } else {
        return "Número inválido";
    } 
  }

  calcularIdade(dataNascimento: string): number {
    const nascimento = new Date(dataNascimento);
    const hoje = new Date();
  
    let idade = hoje.getFullYear() - nascimento.getFullYear();
  
    const mesAtual = hoje.getMonth();
    const diaAtual = hoje.getDate();
  
    const mesNascimento = nascimento.getMonth();
    const diaNascimento = nascimento.getDate();
  
    if (mesAtual < mesNascimento || (mesAtual === mesNascimento && diaAtual < diaNascimento)) {
      idade--;
    }
    return idade;
  }

  logout(ev: any)
  {
    if (ev.detail.role === 'confirm')
    {
      localStorage.removeItem('token');
      this.roteante.navigate(['/login']);
    }
    this.popOver.dismiss();
  }

  voltar(): void {
    this.local.back();
  }
}
