import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ProcurarPartidaPageRoutingModule } from './procurar-partida-routing.module';

import { ProcurarPartidaPage } from './procurar-partida.page';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ProcurarPartidaPageRoutingModule,
    SharedModule
  ],
  declarations: [ProcurarPartidaPage]
})
export class ProcurarPartidaPageModule {}
