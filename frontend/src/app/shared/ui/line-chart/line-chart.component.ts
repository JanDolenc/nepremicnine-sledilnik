import { Component, Input } from '@angular/core';
import { BaseChartDirective } from 'ng2-charts';

@Component({
  selector: 'app-line-chart',
  standalone: true,
  imports: [BaseChartDirective],
  templateUrl: './line-chart.component.html',
})
export class LineChartComponent {
  @Input({ required: true }) chartData!: any[];
  lineChartOptions!: any;
  lineChartData!: any;

  ngOnInit(): void {
    this.lineChartOptions = { responsive: true };
    this.lineChartData = {
      labels: this.chartData.map((item) => item.x_axis),
      datasets: [
        {
          data: this.chartData.map((item) => item.data),
          label: 'Cena',
          tension: 0.3,
        },
      ],
    };
  }
}
