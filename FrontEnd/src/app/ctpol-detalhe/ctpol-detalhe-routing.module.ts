import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CtpolDetalhePage } from './ctpol-detalhe.page';

const routes: Routes = [
  {
    path: '',
    component: CtpolDetalhePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class CtpolDetalhePageRoutingModule {}
