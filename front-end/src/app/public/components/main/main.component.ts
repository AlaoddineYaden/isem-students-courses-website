import { Component } from '@angular/core';
import { HttpService } from '../../services/http.service';
import { Year } from 'src/app/models/Year';
import { AlertData } from 'src/app/shared/components/alert/alert.component';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {
  public isFetchingItems:boolean = true;
  years: Year[] = [];
  alertData: AlertData | undefined = {
    message: "S'il vous plaît, attendez", type: "loading"
  };

  constructor(private httpService:HttpService){}
 
  ngOnInit(): void {
    this.alertData = {
      type: 'loading',
      message: 'loading',
    };
    this.httpService.getAllYearsWithAllSectors().then(data => {
      this.isFetchingItems = false
      this.years = data
      console.log(data)
      this.alertData = {
        type: 'success',
        message: "success",
      }
    }).catch(() => {
      this.alertData = { message: "Erreur lors de la récupération des données", type: "error" }
    }).finally(() => setTimeout(() => this.alertData = undefined, 3000));
  }



  // getAllYearsWithAllSectors() {
  //   this.httpService.getAllYearsWithAllSectors().then(data => {
  //     this.years = data
  //     this.alertData = undefined
  //   }).catch(() => {
  //     this.alertData = { message: "Erreur lors de la récupération des données", type: "error" }
  //   }).finally(() => setTimeout(() => this.alertData = undefined, 3000));
  // }
}
