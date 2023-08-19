import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, first } from 'rxjs';
import { Course } from 'src/app/models/Cours';
import { Exam } from 'src/app/models/Exam';
import { Subject } from 'src/app/models/Subject';
import { Year } from 'src/app/models/Year';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { }

  getAllYearsWithAllSectors(): Promise<Year[]> {
    return new Promise<Year[]>((resolve, reject) => {
      let host = `${environment.API_URL}/get_years_with_sectors/`;
      this.http.get<Year[]>(host)
      .pipe(first())
        .subscribe({
          next: (d: Year[] | PromiseLike<Year[]>) => resolve(d),
          error: (_: any) => reject(),
        })
    });
  }
  getSubjectsBySector(id:number): Promise<Subject[]> {
    return new Promise<Subject[]>((resolve, reject) => {
      let host = `${environment.API_URL}/get_subjects_by_sector/${id}/`;
      this.http.get<Subject[]>(host)
      .pipe(first())
        .subscribe({
          next: (d: Subject[] | PromiseLike<Subject[]>) => resolve(d),
          error: (_: any) => reject(),
        })
    });
  }
  getCoursesBySubject(id:number): Promise<any> {
    return new Promise<any>((resolve, reject) => {
      let host = `${environment.API_URL}/get_courses_and_exams_by_subject/${id}/`;
      this.http.get<any>(host)
      .pipe(first())
        .subscribe({
          next: (d: any | PromiseLike<any>) => resolve(d),
          error: (_: any) => reject(),
        })
    });
  }
  getExamsBySubject(id:number): Promise<any> {
    return new Promise<any>((resolve, reject) => {
      let host = `${environment.API_URL}/get_courses_and_exams_by_subject/${id}/`;
      this.http.get<any>(host)
      .pipe(first())
        .subscribe({
          next: (d: any | PromiseLike<any>) => resolve(d),
          error: (_: any) => reject(),
        })
    });
  }

  getCurrentYear(): number {
    return new Date().getFullYear();
  }
  getCurrentTime(): string {
    const currentTime = new Date();
    const hours = currentTime.getHours().toString().padStart(2, '0');
    const minutes = currentTime.getMinutes().toString().padStart(2, '0');
    const seconds = currentTime.getSeconds().toString().padStart(2, '0');
    return `${hours}:${minutes}:${seconds}`;
  }
  
  // getAllYearsWithAllSectors(): Observable<Year[]> {
  //   let host = "${environment.API_URL}/get_years_with_sectors/";
  //   return this.http.get<Year[]>(host);
  // }
}
