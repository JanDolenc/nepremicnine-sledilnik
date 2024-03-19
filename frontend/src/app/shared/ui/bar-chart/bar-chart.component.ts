import { Component, Input } from '@angular/core';
import { BaseChartDirective } from 'ng2-charts';

@Component({
  selector: 'app-bar-chart',
  standalone: true,
  imports: [BaseChartDirective],
  templateUrl: './bar-chart.component.html',
})
export class BarChartComponent {
  @Input({ required: true }) chartData!: any[];
  barChartOptions!: any;
  barChartData!: any;
}
