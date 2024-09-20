import { Injectable, signal } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class MobileMenuService {
  constructor() {}

  isMobileMenuOpen = signal<boolean>(false);

  open(): void {
    this.isMobileMenuOpen.set(true);
  }

  close(): void {
    this.isMobileMenuOpen.set(false);
  }
}
