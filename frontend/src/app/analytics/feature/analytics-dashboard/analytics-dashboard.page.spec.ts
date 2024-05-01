import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalyticsDashboardPage } from './analytics-dashboard.page';

describe('AnalyticsDashboardPage', () => {
  let component: AnalyticsDashboardPage;
  let fixture: ComponentFixture<AnalyticsDashboardPage>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AnalyticsDashboardPage],
    }).compileComponents();

    fixture = TestBed.createComponent(AnalyticsDashboardPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
