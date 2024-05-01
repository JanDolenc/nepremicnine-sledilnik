import { Component, Input, OnInit } from '@angular/core';
import { BaseChartDirective } from 'ng2-charts';

@Component({
  selector: 'app-doughnut-chart',
  standalone: true,
  imports: [BaseChartDirective],
  templateUrl: './doughnut-chart.component.html',
})
export class DoughnutChartComponent implements OnInit {
  @Input({ required: true }) doughnutChartData!: any;
  @Input() customChartOptions!: any;
  doughnutChartOptions!: any;

  ngOnInit(): void {
    console.log('this is doughnutdata IN graph', this.doughnutChartData);
    this.doughnutChartOptions = {
      responsive: true,
      locale: 'sl',
      plugins: {
        tooltip: {
          position: 'nearest',
          backgroundColor: 'rgba(238, 238, 238, 1)',
          titleColor: 'rgba(18, 18, 18, 1)',
          bodyColor: 'rgba(18, 18, 18, 1)',
          titleFont: {
            size: 15,
          },
          bodyFont: {
            size: 16,
          },
        },
        legend: {
          display: false,
        },
      },

      ...this.customChartOptions,
    };
  }
}
