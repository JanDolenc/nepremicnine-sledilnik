import { Component, inject } from '@angular/core';
import { RouterLink } from '@angular/router';

import { MobileMenuService } from '../../data-access/mobile-menu.service';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './header.component.html',
})
export class HeaderComponent {
  mobileMenuService: MobileMenuService = inject(MobileMenuService);
}
