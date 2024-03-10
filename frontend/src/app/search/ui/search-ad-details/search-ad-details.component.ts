import { Component, Input } from '@angular/core';
import { SearchAdItemComponent } from '../search-ad-item/search-ad-item.component';

import { Ad } from '../../utils/ad';
import { isAdActive } from '../../utils/search-helpers';

@Component({
  selector: 'app-search-ad-details',
  standalone: true,
  imports: [SearchAdItemComponent],
  templateUrl: './search-ad-details.component.html',
})
export class SearchAdDetailsComponent {
  @Input({ required: true }) ad!: Ad;

  isAdActive = isAdActive;
}
