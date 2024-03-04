import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Ad } from '../utils/ad';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class SearchService {
  constructor(private http: HttpClient) {}

  /* GET ad details from the server */
  getAdDetails(url: string): Observable<Ad> {
    return this.http.get<Ad>(`${environment.apiUrl}/search/oglas/?url=${url}`);
  }
}
