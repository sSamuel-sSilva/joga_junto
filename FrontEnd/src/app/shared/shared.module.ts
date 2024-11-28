import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';

import { TypeaheadComponent } from './typeahead/typeahead.component';
import { FiltroRadio } from './filtro-select/filtroradio.component';

@NgModule({
  declarations: [TypeaheadComponent, FiltroRadio], // Declara o componente
  imports: [
    CommonModule,
    FormsModule,
    IonicModule
  ],
  exports: [TypeaheadComponent, FiltroRadio] // Torna o componente utilizável em outros módulos
})
export class SharedModule {}