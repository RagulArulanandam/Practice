import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { PriceDetails } from '../Entities/ISymbols';

@Injectable({
  providedIn: 'root'
})
export class ApiServiceService {

  constructor(private http: HttpClient) { }

  url: string = "https://api.gold-api.com/price/"; 


  getPrice(symbol: string):Observable<( PriceDetails)> {
    return this.http.get(this.url + symbol)as Observable<PriceDetails>;
  }
}
