import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { SearchBarComponent } from '../../ui/search-bar/search-bar.component';

@Component({
  selector: 'app-search-interface',
  standalone: true,
  imports: [SearchBarComponent],
  templateUrl: './search-interface.page.html',
})
export class SearchInterfacePage {
  constructor(private router: Router) {}

  navigateToResultPage(url: string) {
    let encodeUrl = encodeURIComponent(url);
    this.router.navigate([`/search/url/${encodeUrl}`]);
  }
}
