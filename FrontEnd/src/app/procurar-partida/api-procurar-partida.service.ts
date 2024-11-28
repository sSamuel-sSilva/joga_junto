import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiProcurarPartidaService {

  private apiUrl = "http://localhost:8000";

  constructor(private http: HttpClient) { }

  procurar_partida(token: string, modalidade: number, ctpol: number)
  {
    const headers = new HttpHeaders({
      Authorization: `Token ${token}`
    });

  let url = `${this.apiUrl}/api_partida/agendar_buscar_partida/`;
  const params = [];

  if (modalidade !== 0 || modalidade === null) {
    params.push(`modalidade=${modalidade}`);
  }
  if (ctpol !== 0 || ctpol === null) {
    params.push(`ctpol=${ctpol}`);
  }

  if (params.length > 0) {
    url += `?${params.join('&')}`;
  }

  console.log('Montando URL:', url);

  return this.http.get(url, { headers });

  }

  ctpols_proximos(token: string): Observable<any>
  {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`,
    });
    
    return this.http.get(`${this.apiUrl}/api_ctpol/ctpols_prox`, { headers });
  }

}
