import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiLoginService {

  private apiUrl = "http://localhost:8000";

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any>
  {
    return this.http.post(`${this.apiUrl}/auth/login`, {username, password});
  }
}
