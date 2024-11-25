import { TestBed } from '@angular/core/testing';

import { ApiCadastroService } from './api-cadastro.service';

describe('ApiCadastroService', () => {
  let service: ApiCadastroService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiCadastroService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
