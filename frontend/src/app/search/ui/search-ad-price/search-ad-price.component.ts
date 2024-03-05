import { Component, Input, OnInit } from '@angular/core';

import { SearchAdItemComponent } from '../search-ad-item/search-ad-item.component';
import { Price } from '../../utils/ad';

@Component({
  selector: 'app-search-ad-price',
  standalone: true,
  imports: [SearchAdItemComponent],
  templateUrl: './search-ad-price.component.html',
})
export class SearchAdPriceComponent implements OnInit {
  @Input({ required: true }) price_data!: Price[];

  maxPrice: number = 0;
  minPrice: number = 0;
  currentPrice: number = 0;

  ngOnInit(): void {
    this.minPrice = Math.min(...this.price_data.map((item) => item.cena));

    this.maxPrice = Math.max(...this.price_data.map((item) => item.cena));

    this.currentPrice = this.price_data[this.price_data.length - 1].cena;
  }
}
