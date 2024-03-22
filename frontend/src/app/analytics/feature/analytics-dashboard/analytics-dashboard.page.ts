import { Component, OnInit } from '@angular/core';
import { AnalyticsMedianChartComponent } from '../../ui/analytics-median-chart/analytics-median-chart.component';
import { AnalyticsService } from '../../data-access/analytics.service';
import { Median } from '../../utils/median';
import { getCurrentYearMonth } from '../../utils/analytics-helpers';
import { ActiveAd } from '../../utils/active-ads';

@Component({
  selector: 'app-analytics-dashboard',
  standalone: true,
  imports: [AnalyticsMedianChartComponent],
  templateUrl: './analytics-dashboard.page.html',
})
export class AnalyticsDashboardPage implements OnInit {
  constructor(private analyticsService: AnalyticsService) {}

  median!: Median;
  activeAds!: ActiveAd[];

  ngOnInit(): void {
    this.getMedian();
    this.getActiveAds();

    setTimeout(() => {
      console.log(this.activeAds);
      const result = this.sumActiveAds();
      console.log('result', result);
    }, 1000);
  }

  getMedian(): void {
    this.analyticsService
      .getMedian()
      .subscribe((median) => (this.median = median));
  }

  getActiveAds(): void {
    this.analyticsService
      .getActiveAds(getCurrentYearMonth())
      .subscribe((activeAds) => (this.activeAds = activeAds));
  }

}
