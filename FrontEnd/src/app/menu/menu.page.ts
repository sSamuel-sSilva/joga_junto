import { Component, OnInit } from '@angular/core';
import { ApiMenuService } from './api-menu.service';
import { CtpolVitrine } from '../types/ctpol_vitrine';
import { IonRouterOutlet, MenuController } from '@ionic/angular';
import { Router } from '@angular/router';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.page.html',
  styleUrls: ['./menu.page.scss'],
})

export class MenuPage implements OnInit {
  
  constructor(private ApiMenuService: ApiMenuService, private menuCtrl: MenuController, private roteante: Router) { }

  ctpols_proximos: CtpolVitrine[] = [];
  nome_usuario: string | undefined;

  ngOnInit() 
  {
    this.esta_logado();
    this.puxar_ctpols_proximos();
  }

  ionViewWillEnter(): void 
  {
    this.esta_logado();
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

  puxar_ctpols_proximos()
  {
    const token = localStorage.getItem('token');
    if (token != null)
    {
      this.ApiMenuService.ctpols_proximos(token).subscribe({
        next: (data: any) => {
          
          const nome = data.usuario.split(' ');

          this.nome_usuario = nome[0];
          
          data.ctpol.forEach((d: any)=>{
            this.ctpols_proximos.push({
              id: d.id,
              nome: d.nome,
              residencia: d.residencia,
              rua: d.rua,
              numero: d.numero,
              avaliacao: d.avaliacao
            })
          })

          console.log(this.ctpols_proximos);

        }, error: (err)=> {
          console.error("Erro em carregar ctpols_proximos:", err);
        }
      })
    } else {
      console.log("Token inexistente.");
    }
  }

  openMenu() {
    this.menuCtrl.open();
  }

  detalhado(id: number)
  {
    this.roteante.navigate(['/ctpol-detalhe', id]);
  }
}
