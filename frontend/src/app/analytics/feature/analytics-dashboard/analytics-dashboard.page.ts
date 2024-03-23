import { Component, OnInit } from '@angular/core';
import { AnalyticsMedianChartComponent } from '../../ui/analytics-median-chart/analytics-median-chart.component';
import { AnalyticsService } from '../../data-access/analytics.service';
import { Median } from '../../utils/median';
import {
  getCurrentYearMonth,
  groupAdsRegijaVrsta,
} from '../../utils/analytics-helpers';
import { ActiveAd, RegijaVrstaCount } from '../../utils/active-ads';
import { BarChartComponent } from '../../../shared/ui/bar-chart/bar-chart.component';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-analytics-dashboard',
  standalone: true,
  imports: [AnalyticsMedianChartComponent, BarChartComponent, DatePipe],
  templateUrl: './analytics-dashboard.page.html',
})
export class AnalyticsDashboardPage implements OnInit {
  constructor(private analyticsService: AnalyticsService) {}

  median!: Median;
  activeAds!: ActiveAd[];

  hisaSum: number = 0;
  stanovanjeSum: number = 0;
  adsGroupedRegijaVrsta: RegijaVrstaCount[] = [];
  adsByRegion: any;
  customChartOptions: any = {
    scales: {
      x: {
        stacked: true,
        ticks: {
          font: {
            size: 16,
          },
        },
      },
      y: {
        stacked: true,
        title: {
          display: true,
          text: 'Št. aktivnih oglasov',
          font: {
            size: 13,
          },
        },
        ticks: {
          font: {
            size: 16,
          },
        },
      },
    },
  };

  today = new Date();

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

    setTimeout(() => {
      this.adsByRegion = {
        labels: [
          'Gorenjska',
          'J. Primorska',
          'LJ-mesto',
          'LJ-okolica',
          'Podravska',
        ],
        datasets: [
          {
            data: this.adsGroupedRegijaVrsta
              .filter((item) => item.vrsta === 'Hiša')
              .map((item) => item.count),

            label: 'Hiša',
          },
          {
            data: this.adsGroupedRegijaVrsta
              .filter((item) => item.vrsta === 'Stanovanje')
              .map((item) => item.count),

            label: 'Stanovanje',
          },
        ],
      };
    }, 2000);
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
