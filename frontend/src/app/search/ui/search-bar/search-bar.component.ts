import { Component, EventEmitter, Output } from '@angular/core';
import {
  ReactiveFormsModule,
  FormGroup,
  FormControl,
} from '@angular/forms';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './search-bar.component.html',
})
export class SearchBarComponent {
  @Output() searchEvent = new EventEmitter<string>();

  searchForm = new FormGroup({
    url: new FormControl('', [
    ]),
  });

  onSubmit() {
    console.warn('submited');
    if (this.searchForm.valid) {
      console.warn('submited AND valid', this.searchForm.value.url);

      this.searchEvent.emit(this.searchForm.value.url || '');
    }
  }

  }
}
