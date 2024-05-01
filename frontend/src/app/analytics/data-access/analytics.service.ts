import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { Median } from '../utils/median';
import { ActiveAd } from '../utils/active-ads';
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

  /* GET active ads by region */
  getActiveAds(yearMonth: {
    year: number;
    month: number;
  }): Observable<ActiveAd[]> {
    const options = {
      params: new HttpParams()
        .set('year', yearMonth.year)
        .set('month', yearMonth.month),
    };

    return this.http.get<ActiveAd[]>(
      `${environment.apiUrl}/analytics/active-ads`,
      options
    );
  }
}
