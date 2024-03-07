import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Ad, SimilarAds } from '../utils/ad';
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

  /* GET similar ads from the server */
  getSimilarAds(ad: Ad): Observable<SimilarAds> {
    const options = {
      params: new HttpParams()
        .set('id', ad.id)
        .set('regija', ad.regija)
        .set('vrsta', ad.vrsta)
        .set('velikost_min', ad.velikost)
        .set('cena_max', ad.price_data[ad.price_data.length - 1].cena),
    };

    return this.http.get<SimilarAds>(
      `${environment.apiUrl}/search/similar/oglasi`,
      options
    );
  }
}
