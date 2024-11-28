import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ProcurarPartidaPage } from './procurar-partida.page';

const routes: Routes = [
  {
    path: '',
    component: ProcurarPartidaPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ProcurarPartidaPageRoutingModule {}
