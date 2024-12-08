import { Component, Input, OnInit } from '@angular/core';
import { BaseChartDirective } from 'ng2-charts';

@Component({
  selector: 'app-bar-chart',
  standalone: true,
  imports: [BaseChartDirective],
  templateUrl: './bar-chart.component.html',
})
export class BarChartComponent implements OnInit {
  @Input({ required: true }) barChartData!: any;
  @Input() customChartOptions!: any;
  barChartOptions!: any;

  ngOnInit(): void {
    this.barChartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      aspectRatio: 0.8,
      locale: 'sl',
      scales: {
        x: {
          ticks: {
            font: {
              size: 16,
            },
          },
        },
        y: {
          title: {
            display: true,
            text: 'Cena  €',
            font: {
              size: 14,
            },
          },
          ticks: {
            font: {
              size: 16,
            },
          },
        },
      },
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
