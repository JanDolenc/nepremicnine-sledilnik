import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchShortcutComponent } from './search-shortcut.component';

describe('SearchShortcutComponent', () => {
  let component: SearchShortcutComponent;
  let fixture: ComponentFixture<SearchShortcutComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchShortcutComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SearchShortcutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
