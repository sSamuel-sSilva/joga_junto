import { TestBed } from '@angular/core/testing';

import { ApiCtpolDetalheService } from './api-ctpol-detalhe.service';

describe('ApiCtpolDetalheService', () => {
  let service: ApiCtpolDetalheService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiCtpolDetalheService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
