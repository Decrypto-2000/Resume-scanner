import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ResumeUploadComponent } from './resume-upload/resume-upload.component';

const routes: Routes = [
  { path: 'upload', component: ResumeUploadComponent },
  { path: '', redirectTo: 'upload', pathMatch: 'full' }, // optional default route
  { path: '**', redirectTo: 'upload' } // optional wildcard route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
