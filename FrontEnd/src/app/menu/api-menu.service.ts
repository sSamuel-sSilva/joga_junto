import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class ApiMenuService {

  private apiUrl = "http://localhost:8000";

  constructor(private http: HttpClient) { }

  ctpols_proximos(token: string): Observable<any>
  {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`,
    });
    
    return this.http.get(`${this.apiUrl}/api_ctpol/ctpols_prox`, { headers });
  }
}
