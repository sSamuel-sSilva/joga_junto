import { TestBed } from '@angular/core/testing';

import { ApiGeralService } from './api-geral.service';

describe('ApiGeralService', () => {
  let service: ApiGeralService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiGeralService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
