import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  ReactiveFormsModule,
  FormGroup,
  FormControl,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './search-bar.component.html',
})
export class SearchBarComponent {
  @Output() searchEvent = new EventEmitter<string>();

  searchForm = new FormGroup({
    url: new FormControl('', [
      Validators.required,
      Validators.minLength(6),
      Validators.maxLength(230),
    ]),
  });

  onSubmit() {
    console.warn('submited');
    if (this.searchForm.valid) {
      console.warn('submited AND valid', this.searchForm.value.url);

      this.searchEvent.emit(this.searchForm.value.url || '');
    }
  }

  public get url() {
    return this.searchForm.get('url');
  }

  }
}
