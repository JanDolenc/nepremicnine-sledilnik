import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchInstructionsComponent } from './search-instructions.component';

describe('SearchInstructionsComponent', () => {
  let component: SearchInstructionsComponent;
  let fixture: ComponentFixture<SearchInstructionsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchInstructionsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SearchInstructionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
