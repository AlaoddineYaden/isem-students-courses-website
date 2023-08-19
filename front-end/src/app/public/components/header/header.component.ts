import { Component } from '@angular/core';
import { HttpService } from '../../services/http.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  currentYear: number = 0;
  currentTime: string='';
  constructor(private http: HttpService) {
    this.currentYear = this.http.getCurrentYear();
    setInterval(() => {
      this.currentTime = this.http.getCurrentTime();
    }, 1000); // Update time every second
  }

}
