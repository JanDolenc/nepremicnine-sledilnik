import { Component, Input } from '@angular/core';
import { CurrencyPipe, DatePipe, DecimalPipe } from '@angular/common';

@Component({
  selector: 'app-search-ad-item',
  standalone: true,
  imports: [DatePipe, CurrencyPipe, DecimalPipe],
  templateUrl: './search-ad-item.component.html',
})
export class SearchAdItemComponent {
  @Input() label: string | undefined;
  @Input({ required: true }) value!: any;
  // avaiable formats: date, price, sq-meter, string
  @Input() format: string = 'string';
  // custom class for adding styling - bg color
  @Input() customClass: string = 'bg-neutral-100';
}
