import { Component, OnInit } from '@angular/core';
import { MenuController } from '@ionic/angular';
import { ApiLoginService } from './api-login.service'; 
import { Router } from '@angular/router';


@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  dados_validos = false;
  mensagem_erro: string = "Credenciais inválidas.";

  username:string = "";
  password:string = "";

  constructor(private ApiLoginService: ApiLoginService, private menuCtrl: MenuController, private roteante: Router) { }

  ngOnInit() {
    this.menuCtrl.enable(false);
  }

  ionViewWillLeave() {
    this.menuCtrl.enable(true);
  }


  login()
  {
    if (this.username && this.password)
    {
      console.log(this.username);
      console.log(this.password);
      this.ApiLoginService.login(this.username, this.password).subscribe(
        (response: any) => {
          console.log(response);
          localStorage.setItem('token', response.token);
          this.roteante.navigate(['/menu']);

        }, (error) => {
          console.log("erro: " + error);
          this.m_torrada(true, "Crendenciais inválidas");
        }
      )
    } else {
      this.m_torrada(true, "Preencha todos os campos.");
    }
  }  


  m_torrada(situacao: boolean, mensagem: string)
  {
    this.dados_validos = situacao;

    if (situacao)
    {
      this.mensagem_erro = mensagem;
    }
  }
}
