import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalyticsMedianChartComponent } from './analytics-median-chart.component';

describe('AnalyticsMedianChartComponent', () => {
  let component: AnalyticsMedianChartComponent;
  let fixture: ComponentFixture<AnalyticsMedianChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AnalyticsMedianChartComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AnalyticsMedianChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
