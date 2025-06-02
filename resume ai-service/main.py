from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text_from_resume
from skill_matcher import extract_skills, compute_similarity
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with Angular origin if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_resume(resume: UploadFile, job_description: str = Form(...)):
    temp_file = f"temp_{resume.filename}"
    try:
        with open(temp_file, "wb") as f:
            shutil.copyfileobj(resume.file, f)

        resume_text = extract_text_from_resume(temp_file)

    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    skills = extract_skills(resume_text)
    score = compute_similarity(resume_text, job_description)

    return {
        "ExtractedSkills": skills,
        "MatchScore": score
    }

