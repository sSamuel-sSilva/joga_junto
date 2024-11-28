import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ProcurarPartidaPage } from './procurar-partida.page';

describe('ProcurarPartidaPage', () => {
  let component: ProcurarPartidaPage;
  let fixture: ComponentFixture<ProcurarPartidaPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(ProcurarPartidaPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
