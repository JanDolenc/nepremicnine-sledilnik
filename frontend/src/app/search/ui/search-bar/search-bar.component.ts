import {
  Component,
  ElementRef,
  EventEmitter,
  input,
  Output,
  viewChild,
} from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  ReactiveFormsModule,
  FormGroup,
  FormControl,
  Validators,
} from '@angular/forms';

import { SearchBarOptions } from '../../utils/search-helpers';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './search-bar.component.html',
})
export class SearchBarComponent {
  @Output() searchEvent = new EventEmitter<string>();

  /**
   * Search bar component options
   *
   * `layout`: `horizontal` or `vertical`,
   *
   * `placeholderText`: custom string,
   *
   * `miniButton`: `true` or `false`
   */
  options = input<SearchBarOptions>({
    layout: 'horizontal',
    placeholderText: 'Novo iskanje',
    miniButton: false,
  });

  searchForm = new FormGroup({
    url: new FormControl('', [
      Validators.required,
      Validators.minLength(6),
      Validators.maxLength(230),
    ]),
  });

  onSubmit() {
    if (this.searchForm.valid) {
      this.searchEvent.emit(this.searchForm.value.url || '');
    }
  }

  searchInput = viewChild<ElementRef>('search');

  clearSearchForm(): void {
    if (this.url !== null) {
      this.url.reset();
      this.searchInput()?.nativeElement.focus();
    }
  }

  public get url() {
    return this.searchForm.get('url');
  }
}
