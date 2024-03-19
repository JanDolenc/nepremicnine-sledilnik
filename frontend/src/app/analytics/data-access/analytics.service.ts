import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { Median } from '../utils/median';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class AnalyticsService {
  constructor(private http: HttpClient) {}

  /* GET median prices by region */
  getMedian(): Observable<Median> {
    return this.http.get<Median>(`${environment.apiUrl}/analytics/median`);
  }
}
