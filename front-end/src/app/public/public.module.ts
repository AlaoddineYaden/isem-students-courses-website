import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PublicRoutingModule } from './public-routing.module';
import { ContainerComponent } from './components/container/container.component';
import { HeaderComponent } from './components/header/header.component';
import { MainComponent } from './components/main/main.component';
import { HttpClientModule } from '@angular/common/http';
import { SubjectsComponent } from './components/subjects/subjects.component';
import { SharedModule } from '../shared/shared.module';
import { CoursesExamsComponent } from './components/courses-exams/courses-exams.component';


@NgModule({
  declarations: [
    ContainerComponent,
    HeaderComponent,
    MainComponent,
    SubjectsComponent,
    CoursesExamsComponent
  ],
  imports: [
    CommonModule,
    PublicRoutingModule,
    HttpClientModule,
    SharedModule,
  ]
})
export class PublicModule { }
