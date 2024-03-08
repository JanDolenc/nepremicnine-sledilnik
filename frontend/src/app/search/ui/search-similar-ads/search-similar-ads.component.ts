import { Component, Input } from '@angular/core';

import { SimilarAd } from '../../utils/ad';
import { CurrencyPipe, DecimalPipe } from '@angular/common';

@Component({
  selector: 'app-search-similar-ads',
  standalone: true,
  imports: [DecimalPipe, CurrencyPipe],
  templateUrl: './search-similar-ads.component.html',
})
export class SearchSimilarAdsComponent {
  @Input({ required: true }) similarAds!: SimilarAd[];

  ngOnInit() {
    console.log('this are simialr ADS on dest -- ', this.similarAds);
  }
}
