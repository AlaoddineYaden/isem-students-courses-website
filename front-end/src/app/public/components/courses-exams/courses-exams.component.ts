import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subject } from 'rxjs';
import { AlertData } from 'src/app/shared/components/alert/alert.component';
import { HttpService } from '../../services/http.service';
import { Exam } from 'src/app/models/Exam';
import { Course } from 'src/app/models/Cours';

@Component({
  selector: 'app-courses-exams',
  templateUrl: './courses-exams.component.html',
  styleUrls: ['./courses-exams.component.css']
})
export class CoursesExamsComponent {
  subjectId: number = 1;
  public isFetchingItems:boolean = true;
  public isFetchingItems2:boolean = true;
  exams: Exam[] = [];
  coures: Course[] = [];

  alertData: AlertData | undefined = {
    message: "S'il vous plaît, attendez", type: "loading"
  };
  constructor(private route: ActivatedRoute,private httpService:HttpService) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.subjectId = params['id'];
      this.alertData = {
        type: 'loading',
        message: 'loading',
      };
      this.httpService.getCoursesBySubject(this.subjectId).then(data => {
        this.isFetchingItems = false
        this.coures = data['courses']
        console.log(data)
        this.alertData = {
          type: 'success',
          message: "success",
        }
      }).catch(() => {
        this.alertData = { message: "Erreur lors de la récupération des données", type: "error" }
      }).finally(() => setTimeout(() => this.alertData = undefined, 3000));
    });
    this.route.params.subscribe(params => {
      this.subjectId = params['id'];
      this.alertData = {
        type: 'loading',
        message: 'loading',
      };
      this.httpService.getExamsBySubject(this.subjectId).then(data => {
        this.isFetchingItems2 = false
        this.exams = data['exams']
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
