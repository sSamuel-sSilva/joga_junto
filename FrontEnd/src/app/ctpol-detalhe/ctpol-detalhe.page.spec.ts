import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CtpolDetalhePage } from './ctpol-detalhe.page';

describe('CtpolDetalhePage', () => {
  let component: CtpolDetalhePage;
  let fixture: ComponentFixture<CtpolDetalhePage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(CtpolDetalhePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
