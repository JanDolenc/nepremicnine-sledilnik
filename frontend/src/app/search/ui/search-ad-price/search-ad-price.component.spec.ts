import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchAdPriceComponent } from './search-ad-price.component';

describe('SearchAdPriceComponent', () => {
  let component: SearchAdPriceComponent;
  let fixture: ComponentFixture<SearchAdPriceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchAdPriceComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SearchAdPriceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
