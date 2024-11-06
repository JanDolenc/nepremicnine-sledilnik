import { Component, OnInit } from '@angular/core';
import { DatePipe } from '@angular/common';

import { AnalyticsMedianChartComponent } from '../../ui/analytics-median-chart/analytics-median-chart.component';
import { AnalyticsService } from '../../data-access/analytics.service';
import { Median } from '../../utils/median';

@Component({
  selector: 'app-analytics-dashboard',
  standalone: true,
  imports: [
    AnalyticsMedianChartComponent,
    DatePipe,
  ],
  templateUrl: './analytics-dashboard.page.html',
})
export class AnalyticsDashboardPage implements OnInit {
  constructor(private analyticsService: AnalyticsService) { }

  median!: Median;
  today = new Date();

  ngOnInit(): void {
    this.getMedian();
  }

  getMedian(): void {
    this.analyticsService
      .getMedian()
      .subscribe((median) => (this.median = median));
  }
}

