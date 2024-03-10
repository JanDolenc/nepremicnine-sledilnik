import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchAdDetailsComponent } from './search-ad-details.component';

describe('SearchAdDetailsComponent', () => {
  let component: SearchAdDetailsComponent;
  let fixture: ComponentFixture<SearchAdDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchAdDetailsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SearchAdDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
