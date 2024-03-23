import { Component, OnInit } from '@angular/core';
import { AnalyticsMedianChartComponent } from '../../ui/analytics-median-chart/analytics-median-chart.component';
import { AnalyticsService } from '../../data-access/analytics.service';
import { Median } from '../../utils/median';
import {
  getCurrentYearMonth,
  groupAdsRegijaVrsta,
} from '../../utils/analytics-helpers';
import { ActiveAd, RegijaVrstaCount } from '../../utils/active-ads';

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

  hisaSum: number = 0;
  stanovanjeSum: number = 0;
  adsGroupedRegijaVrsta: RegijaVrstaCount[] = [];
  ngOnInit(): void {
    this.getMedian();
    this.getActiveAds();

    setTimeout(() => {
      console.log(this.activeAds);
      this.sumActiveAds();
      console.log(
        'result',
        this.adsGroupedRegijaVrsta,
        this.stanovanjeSum,
        this.hisaSum,
        this.hisaSum + this.stanovanjeSum
      );
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

  sumActiveAds(): void {
    this.adsGroupedRegijaVrsta = groupAdsRegijaVrsta(this.activeAds);

    this.adsGroupedRegijaVrsta.forEach((item: RegijaVrstaCount) => {
      if (item.vrsta === 'Hiša') {
        this.hisaSum += item.count;
      } else {
        this.stanovanjeSum += item.count;
      }
    });
  }
}
