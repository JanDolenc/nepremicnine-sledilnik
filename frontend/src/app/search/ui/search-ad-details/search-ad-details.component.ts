import { Component, Input } from '@angular/core';
import { Ad } from '../../utils/ad';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-search-ad-details',
  standalone: true,
  imports: [DatePipe],
  templateUrl: './search-ad-details.component.html',
})
export class SearchAdDetailsComponent {
  @Input({ required: true }) ad!: Ad;
}
