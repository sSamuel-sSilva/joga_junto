import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CtPol } from '../types/ctpol';
import { Quadra } from '../types/quadra';
import { PeriodoFuncionamento } from '../types/periodo_funcionamento';
import { AuxPartida } from '../types/aux_partida';
import { ApiCtpolDetalheService } from './api-ctpol-detalhe.service';
import { MenuController } from '@ionic/angular';

@Component({
  selector: 'app-ctpol-detalhe',
  templateUrl: './ctpol-detalhe.page.html',
  styleUrls: ['./ctpol-detalhe.page.scss'],
})
export class CtpolDetalhePage implements OnInit {

  id!: number;

  ctpol: CtPol | undefined;
  quadras: Quadra[] = [];
  periodos_func: PeriodoFuncionamento[] = [];
  aux_partida: AuxPartida[] = [];
  quadra_quant: { modalidade: string; quantidade: number }[] = [];

  constructor(private route: ActivatedRoute, private ApiCtpolDetalheService: ApiCtpolDetalheService, private menuCtrl: MenuController) { }

  ngOnInit() 
  {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    console.log("Peguei o id: " + this.id);
    this.puxar_ctpol()
  }

  puxar_ctpol()
  {
    const token = localStorage.getItem('token');
    if (token != null)
    {
      this.ApiCtpolDetalheService.ctpol(this.id, token).subscribe({
        next: (data: any)=> {

          console.log(data);
          data.ct_pol.contato = this.formatarTelefone(data.ct_pol.contato);
          this.ctpol = data.ct_pol;

          data.quadras.forEach((d:any)=>{
            this.quadras.push({
              modalidade: d.modalidade
            })
          })

          data.periodos_func.forEach((d:any) => {
            this.periodos_func.push({
              dia_da_semana: d.dia_da_semana,
              horario_abertura: d.horario_abertura.slice(0, -3),
              horario_fechamento: d.horario_fechamento.slice(0, -3)
            })
          })

          data.aux_partida.forEach((d:any)=>{
            this.aux_partida.push({
              modalidade: d.modalidade,
              quantidade_minima: d.quantidade_minima,
              valor_final: d.valor_final
            })
          })
          
          console.log(this.ctpol);
          this.quadra_quant = this.contarModalidades(this.quadras);
        }, error: (err) =>
        {
          console.log("Erro em busca o ctpol: " + err);
        }
      })
    }
  }

  openMenu() {
    this.menuCtrl.open();
  }

  formatarTelefone(numero: string) 
  {
    if (numero.length === 11) {
        return numero.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
    } else {
        return "Número inválido";
    } 
  }

  contarModalidades(quadras: Quadra[]): { modalidade: string; quantidade: number }[] {
    const contagem: { [modalidade: string]: number } = {};

    quadras.forEach((quadra) => {
      contagem[quadra.modalidade] = (contagem[quadra.modalidade] || 0) + 1;
    });

    return Object.entries(contagem).map(([modalidade, quantidade]) => ({ modalidade, quantidade }));
  }
}
