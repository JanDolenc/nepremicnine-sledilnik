import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { switchMap } from 'rxjs';

import { SearchService } from '../../data-access/search.service';
import { SearchAdDetailsComponent } from '../../ui/search-ad-details/search-ad-details.component';
import { SearchAdPriceComponent } from '../../ui/search-ad-price/search-ad-price.component';

import { Ad, SimilarAds } from '../../utils/ad';

@Component({
  selector: 'app-search-results',
  standalone: true,
  imports: [SearchAdDetailsComponent, SearchAdPriceComponent],
  templateUrl: './search-results.page.html',
})
export class SearchResultsPage implements OnInit {
  ad!: Ad;
  similarAds!: SimilarAds;

  constructor(
    private route: ActivatedRoute,
    private searchService: SearchService
  ) {}

  ngOnInit(): void {
    this.getData();
  }

  getData(): void {
    const url = decodeURIComponent(
      String(this.route.snapshot.paramMap.get('url'))
    );

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
      .subscribe(
        (similarAds) =>
          // handle the second request response
          (this.similarAds = similarAds)
      );
  }
}
