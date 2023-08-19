import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpService } from '../../services/http.service';
import { Sector } from 'src/app/models/Sector';
import { AlertData } from 'src/app/shared/components/alert/alert.component';
import { Subject } from 'src/app/models/Subject';

@Component({
  selector: 'app-subjects',
  templateUrl: './subjects.component.html',
  styleUrls: ['./subjects.component.css']
})
export class SubjectsComponent {
  sectorId: number = 1;
  public isFetchingItems:boolean = true;
  subjects: Subject[] = [];

  alertData: AlertData | undefined = {
    message: "S'il vous plaît, attendez", type: "loading"
  };
  constructor(private route: ActivatedRoute,private httpService:HttpService) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.sectorId = params['id'];
      this.alertData = {
        type: 'loading',
        message: 'loading',
      };
      this.httpService.getSubjectsBySector(this.sectorId).then(data => {
        this.isFetchingItems = false
        this.subjects = data
        console.log(data)
        this.alertData = {
          type: 'success',
          message: "success",
        }
      }).catch(() => {
        this.alertData = { message: "Erreur lors de la récupération des données", type: "error" }
      }).finally(() => setTimeout(() => this.alertData = undefined, 3000));
    });
  }
}
