import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = "http://localhost:8000";

  constructor(private http: HttpClient) { }

  modalidades(): Observable<any>
  {
    return this.http.get(`${this.apiUrl}/api_ctpol/modalidade/`)
  }

  locais(): Observable<any>
  {
    return this.http.get(`${this.apiUrl}/api_ctpol/cidade_estado/`)
  }
}