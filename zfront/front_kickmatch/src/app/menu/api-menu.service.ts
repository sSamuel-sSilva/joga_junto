import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiMenuService {

  private apiUrl = "http://localhost:8000";

  constructor(private http: HttpClient) { }

  dados_perfil(): Observable<any>
  {
    return this.http.get(`${this.apiUrl}/auth/visualizar_perfil`);
  }
}
