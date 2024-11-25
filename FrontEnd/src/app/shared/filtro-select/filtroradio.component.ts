import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Item } from 'src/app/types/type';

@Component({
  selector: 'filtro-radio',
  templateUrl: 'filtroradio.component.html',
  styleUrls: ['./filtroradio.component.css']
})

export class FiltroRadio
{
    @Input() itens: Item[] = [];

    @Output() atualizar = new EventEmitter<number>();
    @Output() cancelar = new EventEmitter<void>();

    selecionado: number | undefined;
    itens_filtrados: Item[] = [];

    constructor() {}

    ngOnInit()
    {
        this.itens_filtrados = [...this.itens];
    }

    cancel() {
        return this.cancelar.emit();
    }

    confirm() {
        console.log(this.selecionado);
        return this.atualizar.emit(this.selecionado);
    }

    procurar_item(index: number, item: Item)
    {
        return item.value;
    }

    entrada_pesquisa(ev: any)
    {
        this.lista_filtragem(ev.target.value);
    }

    lista_filtragem(busca: string | undefined)
    {
        if (busca === undefined) 
        {
            this.itens_filtrados = [...this.itens];
        } else {
            const busca_formatada = busca.toLowerCase();
            this.itens_filtrados = this.itens.filter((item) => {
                return item.value.toLowerCase().includes(busca_formatada);
            })
        }
    }
}