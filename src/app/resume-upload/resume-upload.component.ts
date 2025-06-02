import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ResumeService } from '../services/resume.service';

@Component({
  selector: 'app-resume-upload',
  templateUrl: './resume-upload.component.html',
  styleUrls: ['./resume-upload.component.scss']
})
export class ResumeUploadComponent implements OnInit {
  uploadForm: FormGroup;
  resumeFile!: File;
  result: any;

  constructor(private fb: FormBuilder, private resumeService: ResumeService) {
    this.uploadForm = this.fb.group({
      jobDescription: ['', Validators.required]
    });
  }

  ngOnInit(): void {}

  onFileChange(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files?.length) {
      this.resumeFile = input.files[0];
    }
  }

  onSubmit() {
    const jobDescription = this.uploadForm.get('jobDescription')?.value;

    if (!this.resumeFile || !jobDescription.trim()) {
      alert('Please upload resume and enter job description.');
      return;
    }

    this.resumeService.uploadResumeAndJD(this.resumeFile,jobDescription).subscribe({
  next: (res) => {
    this.result = res;
    console.log(this.result); // ✅ This is now valid
  },
  error: (err) => console.error('Upload failed', err)
});

  }
}
