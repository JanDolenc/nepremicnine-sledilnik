import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { SearchService } from '../../data-access/search.service';
import { Ad } from '../../utils/ad';

@Component({
  selector: 'app-search-results',
  standalone: true,
  imports: [],
  templateUrl: './search-results.page.html',
})
export class SearchResultsPage implements OnInit {
  ad: Ad | undefined;

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
