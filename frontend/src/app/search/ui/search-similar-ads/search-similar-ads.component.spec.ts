import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchSimilarAdsComponent } from './search-similar-ads.component';

describe('SearchSimilarAdsComponent', () => {
  let component: SearchSimilarAdsComponent;
  let fixture: ComponentFixture<SearchSimilarAdsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchSimilarAdsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SearchSimilarAdsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
