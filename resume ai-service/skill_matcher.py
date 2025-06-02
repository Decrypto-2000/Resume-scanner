import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

skills_list = [
    "Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go", "PHP",
    "SQL", "NoSQL", "MongoDB", "MySQL", "PostgreSQL", "Docker", "Kubernetes",
    "AWS", "Azure", "Google Cloud", "Machine Learning", "Deep Learning", "Data Science",
    "TensorFlow", "PyTorch", "Scikit-learn", "REST API", "GraphQL", "Linux",
    "Git", "Agile", "Scrum", "DevOps", "CI/CD", "FastAPI", "Flask", "Django",
    "React", "Angular", "Vue.js", "HTML", "CSS", "TypeScript", "Swift", "Objective-C"
]

def extract_skills(text):
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()

    found_skills = set()
    for skill in skills_list:
        if re.search(rf'\b{re.escape(skill.lower())}\b', text_lower):
            found_skills.add(skill)
    return list(found_skills)

def compute_similarity(resume_text, job_description):
    embeddings = model.encode([resume_text, job_description])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(float(score), 2)
