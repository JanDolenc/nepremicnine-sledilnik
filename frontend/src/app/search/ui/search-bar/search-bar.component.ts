import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [],
  templateUrl: './search-bar.component.html',
})
export class SearchBarComponent {
  @Output() searchEvent = new EventEmitter<string>();

  emitUrl(url: string) {
    this.searchEvent.emit(url);
  }
}
