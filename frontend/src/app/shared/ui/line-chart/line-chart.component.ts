import { Component, Input, OnChanges, OnInit } from '@angular/core';
import { BaseChartDirective } from 'ng2-charts';

@Component({
  selector: 'app-line-chart',
  standalone: true,
  imports: [BaseChartDirective],
  templateUrl: './line-chart.component.html',
})
export class LineChartComponent implements OnChanges, OnInit {
  @Input({ required: true }) chartData!: any[];
  lineChartOptions!: any;
  lineChartData!: any;

  ngOnChanges(): void {
    this.lineChartData = {
      labels: this.chartData.map((item) => item.x_axis),
      datasets: [
        {
          data: this.chartData.map((item) => item.data),
          label: 'Cena',
          tension: 0.2,
        },
      ],
    };

  }

  ngOnInit(): void {
    this.lineChartOptions = {
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
    };

  }
}
