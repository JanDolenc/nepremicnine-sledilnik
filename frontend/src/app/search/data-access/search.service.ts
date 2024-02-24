import { Injectable } from '@angular/core';
import { AD } from '../utils/mock-ad';
import { of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SearchService {
  constructor() {}

  getAdDetails(url: string) {
    console.log('SERVICE: value of received url: ', url);
    return of(AD);
  }
}
