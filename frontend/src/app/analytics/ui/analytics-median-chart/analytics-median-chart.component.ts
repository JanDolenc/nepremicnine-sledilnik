import { Component, Input, OnInit } from '@angular/core';
import { BarChartComponent } from '../../../shared/ui/bar-chart/bar-chart.component';
import { Median } from '../../utils/median';

@Component({
  selector: 'app-analytics-median-chart',
  standalone: true,
  imports: [BarChartComponent],
  templateUrl: './analytics-median-chart.component.html',
})
export class AnalyticsMedianChartComponent implements OnInit {
  @Input({ required: true }) median!: Median;
  medianData: any[] = [];
  barChartData: any;

  ngOnInit(): void {
    this.medianData = this.median.median;
    this.barChartData = {
      labels: this.medianData.map((item) => item.regija),
      datasets: [
        {
          data: this.medianData.map((item) => item.hisa),
          label: 'Hiša',
        },
        {
          data: this.medianData.map((item) => item.stanovanje),
          label: 'Stanovanje',
        },
      ],
    };
  }
}
