import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { HeaderComponent } from './shared/ui/header/header.component';
import { MobileMenuComponent } from './shared/ui/mobile-menu/mobile-menu.component';
import { SearchInterfacePage } from './search/feature/search-interface/search-interface.page';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    HeaderComponent,
    SearchInterfacePage,
    MobileMenuComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'frontend';
}
