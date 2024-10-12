import { Component } from '@angular/core';
import { ApiServiceService } from '../../services/api-service.service';
import { PriceDetails } from '../../Entities/ISymbols';




@Component({
  selector: 'app-main-screen',
  templateUrl: './main-screen.component.html',
  styleUrl: './main-screen.component.css'
})
export class MainScreenComponent {

  value: PriceDetails={ name: "",
    price: 0,
    symbol: "",
    updatedAt: "",
    updatedAtReadable:"",};

  ngOnInit() {
    this.getCurrentGoldPrice();
  }
  constructor(private apiService: ApiServiceService) {
  }

  // goldPrice = 20000;

  getCurrentGoldPrice() {
    return this.apiService.getPrice("XAU").subscribe({
      next: (data) => {
        this.value = data;
      },
      error: (err) => {
        console.log(err);
      }
    });
  }

}
