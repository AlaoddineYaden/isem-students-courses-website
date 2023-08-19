import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContainerComponent } from './components/container/container.component';
import { MainComponent } from './components/main/main.component';
import { SubjectsComponent } from './components/subjects/subjects.component';
import { CoursesExamsComponent } from './components/courses-exams/courses-exams.component';

const routes: Routes = [
  { path: 'home', redirectTo: 'home/main', pathMatch: 'full' },

  {
    path: 'home',
    component: ContainerComponent,
    children: [
      { path: 'main', component: MainComponent },
      { path: 'subjects/:id', component: SubjectsComponent },
      { path: 'couses_exams/:id', component: CoursesExamsComponent },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PublicRoutingModule { }
