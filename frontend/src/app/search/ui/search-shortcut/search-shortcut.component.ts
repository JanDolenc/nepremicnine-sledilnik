import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-search-shortcut',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './search-shortcut.component.html',
})
export class SearchShortcutComponent {
  hide: boolean = false;
}
