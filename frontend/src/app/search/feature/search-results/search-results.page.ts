import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { map, switchMap } from 'rxjs';

import { SearchService } from '../../data-access/search.service';
import { SearchAdDetailsComponent } from '../../ui/search-ad-details/search-ad-details.component';
import { SearchAdPriceComponent } from '../../ui/search-ad-price/search-ad-price.component';
import { SearchSimilarAdsComponent } from '../../ui/search-similar-ads/search-similar-ads.component';

import { Ad, SimilarAd } from '../../utils/ad';

@Component({
  selector: 'app-search-results',
  standalone: true,
  imports: [
    SearchAdDetailsComponent,
    SearchAdPriceComponent,
    SearchSimilarAdsComponent,
  ],
  templateUrl: './search-results.page.html',
})
export class SearchResultsPage implements OnInit {
  ad: Ad | undefined;
  // Unnested SimilarAds
  similarAds: SimilarAd[] | undefined;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private searchService: SearchService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      const url = decodeURIComponent(String(params['url']));
      this.getData(url);
    });
  }

  similarAdClicked(referencna_st: string) {
    this.similarAds = undefined;
    this.ad = undefined;
    this.router.navigate([`/search/url/${referencna_st}`]);
  }

  getData(url: string): void {
    /** Make sequential requests
     *
     * getSimilarAds() request needs data from the getAdDetails().
     * getadDetails() -> complete -> getSimilarAds(getAdDetails response)
     */
    // make first request
    this.searchService
      .getAdDetails(url)
      .pipe(
        // when complete run the second request
        switchMap((ad) => {
          this.ad = ad;
          return this.searchService.getSimilarAds(ad);
        })
      )
      // handle the second request response
      .pipe(map((nestedSimilarAds) => nestedSimilarAds.similar_oglasi))
      .subscribe((similarAds) => (this.similarAds = similarAds));
  }
}
