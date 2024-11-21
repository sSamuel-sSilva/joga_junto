import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiCadastroService {

  private apiUrl = "http://localhost:8000";

  constructor(private http: HttpClient) { }

  cadastro(data: any): Observable<any>
  {
    return this.http.post(`${this.apiUrl}/auth/register`, data)
  }
}