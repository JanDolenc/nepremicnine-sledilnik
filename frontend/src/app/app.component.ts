import { Component, inject } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { SearchInterfacePage } from './search/feature/search-interface/search-interface.page';
import { HeaderComponent } from './shared/feature/header/header.component';
import { MobileMenuComponent } from './shared/ui/mobile-menu/mobile-menu.component';
import { SearchShortcutComponent } from './search/ui/search-shortcut/search-shortcut.component';
import { MobileMenuService } from './shared/data-access/mobile-menu.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    HeaderComponent,
    SearchInterfacePage,
    MobileMenuComponent,
    SearchShortcutComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  mobileMenuService: MobileMenuService = inject(MobileMenuService);
}
