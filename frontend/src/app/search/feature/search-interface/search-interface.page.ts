import { Component } from '@angular/core';
import { SearchBarComponent } from '../../ui/search-bar/search-bar.component';

@Component({
  selector: 'app-search-interface',
  standalone: true,
  imports: [SearchBarComponent],
  templateUrl: './search-interface.page.html',
})
export class SearchInterfacePage {
  getAdData(url: string) {
    console.log('this is from parent', url);
  }
}
