import { Routes } from '@angular/router';

import { SearchInterfacePage } from './search/feature/search-interface/search-interface.page';
import { SearchResultsPage } from './search/feature/search-results/search-results.page';
import { AnalyticsDashboardPage } from './analytics/feature/analytics-dashboard/analytics-dashboard.page';

export const routes: Routes = [
  { path: 'search/url/:url', component: SearchResultsPage },
  { path: 'search', component: SearchInterfacePage },
  { path: 'analytics', component: AnalyticsDashboardPage },
  { path: '', redirectTo: '/search', pathMatch: 'full' },
];
