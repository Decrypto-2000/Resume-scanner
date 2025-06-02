import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ResumeService {
  private apiUrl = 'http://localhost:5122/api/Resume/upload';

  constructor(private http: HttpClient) {}

  uploadResumeAndJD(resume: File, jobDescription: string): Observable<any> {
    const formData = new FormData();
    formData.append('ResumeFile', resume);                
    formData.append('JobDescription', jobDescription);    

    return this.http.post<any>(this.apiUrl, formData);
  }
}
