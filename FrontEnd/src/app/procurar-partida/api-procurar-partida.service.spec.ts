import { TestBed } from '@angular/core/testing';

import { ApiProcurarPartidaService } from './api-procurar-partida.service';

describe('ApiProcurarPartidaService', () => {
  let service: ApiProcurarPartidaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiProcurarPartidaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
