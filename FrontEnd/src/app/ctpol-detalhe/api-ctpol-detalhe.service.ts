import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders,  } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiCtpolDetalheService {

  private apiUrl = "http://localhost:8000";

  constructor(private http: HttpClient) { }

  ctpol(id: number, token: string): Observable<any>
  {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`,
    });
    return this.http.get(`${this.apiUrl}/api_ctpol/ctpol_detail/${id}`, { headers })
  }
}
