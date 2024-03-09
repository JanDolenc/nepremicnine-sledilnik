import { Component, EventEmitter, Input, Output } from '@angular/core';

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
  @Output() adClickedEvent = new EventEmitter<string>();

  selectedAd(referencna_st: number) {
    this.adClickedEvent.emit(String(referencna_st));
  }
}
