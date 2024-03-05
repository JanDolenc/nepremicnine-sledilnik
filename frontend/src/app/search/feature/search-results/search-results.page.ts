import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { SearchService } from '../../data-access/search.service';
import { Ad } from '../../utils/ad';
import { SearchAdDetailsComponent } from '../../ui/search-ad-details/search-ad-details.component';
import { SearchAdPriceComponent } from '../../ui/search-ad-price/search-ad-price.component';

@Component({
  selector: 'app-search-results',
  standalone: true,
  imports: [SearchAdDetailsComponent, SearchAdPriceComponent],
  templateUrl: './search-results.page.html',
})
export class SearchResultsPage implements OnInit {
  ad!: Ad;

  constructor(
    private route: ActivatedRoute,
    private searchService: SearchService
  ) {}

  ngOnInit(): void {
    this.getAdDetails();
  }

  getAdDetails(): void {
    const url = decodeURIComponent(
      String(this.route.snapshot.paramMap.get('url'))
    );

    //this.ad = this.searchService.getAdDetails(url);
    this.searchService.getAdDetails(url).subscribe((ad) => (this.ad = ad));

    console.log('in results this is ad from service: ', this.ad);
  }
}
