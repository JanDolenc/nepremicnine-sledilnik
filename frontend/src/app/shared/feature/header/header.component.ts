import { Component, inject } from '@angular/core';
import { Router, RouterLink } from '@angular/router';

import { MobileMenuService } from '../../data-access/mobile-menu.service';
import { SearchBarComponent } from '../../../search/ui/search-bar/search-bar.component';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterLink, SearchBarComponent],
  templateUrl: './header.component.html',
})
export class HeaderComponent {
  router: Router = inject(Router);
  mobileMenuService: MobileMenuService = inject(MobileMenuService);

  navigateToResultPage(url: string) {
    let encodeUrl = encodeURIComponent(url);
    this.router.navigate([`/search/url/${encodeUrl}`]);
  }
}
