import { Component, Input, Output, EventEmitter } from '@angular/core';
import type { OnInit } from '@angular/core';
import { Item } from '../../types/type';

@Component({
    selector: 'app-typeahead',
    templateUrl: 'typeahead.component.html',
    styleUrls: ['./typeahead.component.css']
})

export class TypeaheadComponent implements OnInit 
{
    @Input() itens: Item[] = [];
    @Input() itens_selecionados:  string[] = [];

    @Output() cancelar = new EventEmitter<void>();
    @Output() atualizar = new EventEmitter<string[]>();


    itens_filtrados: Item[] = [];
    trabalhando_valores_selecionados: string[] = [];

    ngOnInit() 
    {
        this.trabalhando_valores_selecionados = [...this.itens_selecionados];
        this.itens_filtrados = [...this.itens];
    }

    cancelar_selecao()
    {
        this.cancelar.emit();
    }

    confirmar_selecao()
    {
        this.atualizar.emit(this.trabalhando_valores_selecionados);
    }

    procurar_itens(index: number, item: Item)
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

    esta_checado(value: string)
    {
        return this.trabalhando_valores_selecionados.find((item) => item === value);
    }

    mudanca_checagem(ev: any)
    {
        const value = ev.target.value; 
        const checado = ev.target.checked; 
        
        if (checado) {
          this.trabalhando_valores_selecionados = [...this.trabalhando_valores_selecionados, value];
          console.log("Dentro de mudanca_checagem verdadeiro: " + this.trabalhando_valores_selecionados);
        } else {
          this.trabalhando_valores_selecionados = this.trabalhando_valores_selecionados.filter((item) => item !== value);
          console.log("Dentro de mudanca_checagem false: " + this.trabalhando_valores_selecionados);
        }
    }
}