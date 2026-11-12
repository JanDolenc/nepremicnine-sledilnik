import { HttpErrorResponse } from '@angular/common/http';
import { Component, DestroyRef, inject, OnInit } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { catchError, EMPTY, map, Observable, of, switchMap } from 'rxjs';

import { SearchService } from '../../data-access/search.service';
import { SearchAdDetailsComponent } from '../../ui/search-ad-details/search-ad-details.component';
import { SearchAdPriceComponent } from '../../ui/search-ad-price/search-ad-price.component';
import { SearchSimilarAdsComponent } from '../../ui/search-similar-ads/search-similar-ads.component';

import { Ad, SimilarAd } from '../../utils/ad';

@Component({
  selector: 'app-search-results',
  standalone: true,
  imports: [
    RouterLink,
    SearchAdDetailsComponent,
    SearchAdPriceComponent,
    SearchSimilarAdsComponent,
  ],
  templateUrl: './search-results.page.html',
})
export class SearchResultsPage implements OnInit {
  state: 'loading' | 'success' | 'not-found' | 'error' = 'loading';
  ad: Ad | undefined;
  // Unnested SimilarAds
  similarAds: SimilarAd[] | undefined;
  similarAdsError = false;

  private destroyRef = inject(DestroyRef);

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private searchService: SearchService
  ) {}

  ngOnInit(): void {
    this.route.params
      .pipe(
        switchMap((params) => {
          const url = decodeURIComponent(String(params['url']));
          return this.getData(url);
        }),
        takeUntilDestroyed(this.destroyRef)
      )
      .subscribe((similarAds) => (this.similarAds = similarAds));
  }

  similarAdClicked(referencna_st: string) {
    this.router.navigate([`/search/url/${referencna_st}`]);
  }

  private getData(url: string): Observable<SimilarAd[]> {
    this.state = 'loading';
    this.ad = undefined;
    this.similarAds = undefined;
    this.similarAdsError = false;

    return this.searchService.getAdDetails(url).pipe(
      switchMap((ad) => {
        this.ad = ad;
        this.state = 'success';

        return this.searchService.getSimilarAds(ad).pipe(
          map((result) => result.similar_oglasi),
          catchError((error: HttpErrorResponse) => {
            this.similarAdsError = error.status !== 404;
            return of<SimilarAd[]>([]);
          })
        );
      }),
      catchError((error: HttpErrorResponse) => {
        this.state = error.status === 404 ? 'not-found' : 'error';
        return EMPTY;
      })
    );
  }
}
