import { Component } from '@angular/core';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {

  public appPages = [
    { title: 'Perfil', url: '/folder/inbox', icon: 'person-outline' },
    { title: 'Criar Partida', url: '/folder/outbox', icon: 'add-outline' },
    { title: 'Pesquisar Partida', url: '/folder/favorites', icon: 'search-outline' },
    { title: 'LogOut', url: '/folder/favorites', icon: 'log-out-outline' },
  ];
  constructor() {}
}