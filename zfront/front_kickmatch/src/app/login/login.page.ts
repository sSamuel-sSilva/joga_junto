import { Component, OnInit } from '@angular/core';
import { ApiLoginService } from './api-login.service'; 
import { MenuController } from '@ionic/angular';
import { NavController } from '@ionic/angular';


@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  constructor(private ApiLoginService: ApiLoginService, private menuCtrl: MenuController, private navCtrl: NavController) { }

  username: string = "";
  password: string = "";

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
      this.ApiLoginService.login(this.username, this.password).subscribe(
        (response: any) => {
          console.log(response);
          localStorage.setItem('token', response.token);
          this.navCtrl.navigateRoot('/menu');

        }, (error) => {
          console.log("erro: " + error);
          alert("Credenciais inválidas")
        }
      )
    } else {
      alert("Preencha todos os campos.")
    }
  }
}
