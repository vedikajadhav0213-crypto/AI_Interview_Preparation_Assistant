import re

def calculate_ats_score(resume_text, skills):

    score = 0

    # Email
    if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume_text):
        score += 10

    # Phone Number
    if re.search(r"\b\d{10}\b", resume_text):
        score += 10

    # Education
    education_keywords = [
        "Bachelor",
        "B.Tech",
        "BE",
        "B.E",
        "Diploma",
        "M.Tech",
        "MCA",
        "BSc",
        "BCA"
    ]

    for word in education_keywords:
        if word.lower() in resume_text.lower():
            score += 15
            break

    # Experience
    experience_keywords = [
        "Experience",
        "Internship",
        "Worked",
        "Project"
    ]

    for word in experience_keywords:
        if word.lower() in resume_text.lower():
            score += 15
            break

    # Skills (Maximum 30)
    score += min(len(skills) * 2, 30)

    # Certifications
    certification_keywords = [
        "Certificate",
        "Certification",
        "Coursera",
        "Udemy",
        "NPTEL"
    ]

    for word in certification_keywords:
        if word.lower() in resume_text.lower():
            score += 10
            break

    # Cap the score at 100
    return min(score, 100)