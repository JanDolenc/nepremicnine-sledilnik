import { Injectable } from '@angular/core';
import { AD } from '../utils/mock-ad';

@Injectable({
  providedIn: 'root',
})
export class SearchService {
  constructor() {}

  getAdData() {
    return AD;
  }
}
