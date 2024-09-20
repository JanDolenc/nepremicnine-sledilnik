import { Component, inject } from '@angular/core';
import { RouterLink } from '@angular/router';

import { MobileMenuService } from '../../data-access/mobile-menu.service';

@Component({
  selector: 'app-mobile-menu',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './mobile-menu.component.html',
})
export class MobileMenuComponent {
  mobileMenuService: MobileMenuService = inject(MobileMenuService);
}
