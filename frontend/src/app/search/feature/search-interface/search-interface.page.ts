import { Component } from '@angular/core';
import { SearchBarComponent } from '../../ui/search-bar/search-bar.component';
import { SearchService } from '../../data-access/search.service';
import { Ad } from '../../utils/ad';

@Component({
  selector: 'app-search-interface',
  standalone: true,
  imports: [SearchBarComponent],
  templateUrl: './search-interface.page.html',
})
export class SearchInterfacePage {
  constructor(private searchService: SearchService) {}

  ad: Ad | undefined;

  getAdData(url: string) {
    console.log('this is from parent', url);

    this.ad = this.searchService.getAdData();

    console.log('this log is from parent value of ad from service ', this.ad);
  }
}
