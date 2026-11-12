import { Component, OnInit } from '@angular/core';

import { AnalyticsMedianChartComponent } from '../../ui/analytics-median-chart/analytics-median-chart.component';
import { AnalyticsService } from '../../data-access/analytics.service';
import { Median } from '../../utils/median';

@Component({
  selector: 'app-analytics-dashboard',
  standalone: true,
  imports: [
    AnalyticsMedianChartComponent,
  ],
  templateUrl: './analytics-dashboard.page.html',
})
export class AnalyticsDashboardPage implements OnInit {
  constructor(private analyticsService: AnalyticsService) { }

  median!: Median;

  ngOnInit(): void {
    this.getMedian();
  }

  getMedian(): void {
    this.analyticsService
      .getMedian()
      .subscribe((median) => (this.median = median));
  }
}
