import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { CtpolDetalhePageRoutingModule } from './ctpol-detalhe-routing.module';

import { CtpolDetalhePage } from './ctpol-detalhe.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    CtpolDetalhePageRoutingModule
  ],
  declarations: [CtpolDetalhePage]
})
export class CtpolDetalhePageModule {}
