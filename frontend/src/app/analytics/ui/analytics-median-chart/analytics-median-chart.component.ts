import { Component, Input } from '@angular/core';
import { BarChartComponent } from '../../../shared/ui/bar-chart/bar-chart.component';
import { Median } from '../../utils/median';

@Component({
  selector: 'app-analytics-median-chart',
  standalone: true,
  imports: [BarChartComponent],
  templateUrl: './analytics-median-chart.component.html',
})
export class AnalyticsMedianChartComponent {
  @Input({ required: true }) median!: Median;
  chartData: any[] = [''];

  ngOnInit() {
    console.log('median values in DESTINATION', this.median);
  }
}
