import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private BASE_URL = 'http://127.0.0.1:8000/api/login';

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any>
    {
      return this.http.post<any>(this.BASE_URL, { username, password });
    }


  
}
