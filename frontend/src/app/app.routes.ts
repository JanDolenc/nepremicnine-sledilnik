import { Routes } from '@angular/router';

import { SearchInterfacePage } from './search/feature/search-interface/search-interface.page';
import { SearchResultsPage } from './search/feature/search-results/search-results.page';

export const routes: Routes = [
  { path: 'search/url/:url', component: SearchResultsPage },
  { path: 'search', component: SearchInterfacePage },
  { path: '', redirectTo: '/search', pathMatch: 'full' },
];
