import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchAdItemComponent } from './search-ad-item.component';

describe('SearchAdItemComponent', () => {
  let component: SearchAdItemComponent;
  let fixture: ComponentFixture<SearchAdItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchAdItemComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SearchAdItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
