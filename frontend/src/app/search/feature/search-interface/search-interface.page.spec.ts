import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchInterfacePage } from './search-interface.page';

describe('SearchInterfaceComponent', () => {
  let component: SearchInterfacePage;
  let fixture: ComponentFixture<SearchInterfacePage>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchInterfacePage],
    }).compileComponents();

    fixture = TestBed.createComponent(SearchInterfacePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
