import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';

import { SearchBarComponent } from '../../ui/search-bar/search-bar.component';
import { SearchInstructionsComponent } from '../../ui/search-instructions/search-instructions.component';

@Component({
  selector: 'app-search-interface',
  standalone: true,
  imports: [RouterLink, SearchBarComponent, SearchInstructionsComponent],
  templateUrl: './search-interface.page.html',
})
export class SearchInterfacePage {
  // Replace these placeholder URLs with listings available in the app's archive.
  readonly exampleListings = [
    { label: 'Stanovanje v Ljubljani', url: 'https://www.nepremicnine.net/oglasi-prodaja/lj-center-bellevue-frankopanska-stanovanje_6607086/' },
    { label: 'Hiša na Gorenjskem', url: 'https://www.nepremicnine.net/oglasi-prodaja/bodesce-hisa_6387983/' },
    { label: 'Stanovanje v Mariboru', url: 'https://www.nepremicnine.net/oglasi-prodaja/studenci-maribor-dravski-kristali-stanovanje_6786486/' },
  ];

  constructor(private router: Router) {}

  navigateToResultPage(url: string) {
    let encodeUrl = encodeURIComponent(url);
    this.router.navigate([`/search/url/${encodeUrl}`]);
  }
}
