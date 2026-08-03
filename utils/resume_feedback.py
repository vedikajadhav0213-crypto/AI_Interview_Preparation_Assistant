def get_resume_feedback(ats_score, resume_text):

    suggestions = []
    missing_skills = []

    resume = resume_text.lower()

    skills = [
        "python",
        "sql",
        "flask",
        "machine learning",
        "git",
        "github",
        "docker",
        "aws"
    ]

    for skill in skills:
        if skill not in resume:
            missing_skills.append(skill.title())

    if ats_score >= 90:
        suggestions = [
            "Excellent resume!",
            "Keep your resume updated.",
            "Add your latest projects.",
            "Tailor your resume for each job."
        ]

    elif ats_score >= 70:
        suggestions = [
            "Good resume.",
            "Add more technical skills.",
            "Include certifications.",
            "Describe your projects in more detail.",
            "Add measurable achievements."
        ]

    else:
        suggestions = [
            "Improve your resume formatting.",
            "Add missing technical skills.",
            "Include internships or projects.",
            "Use more ATS keywords.",
            "Add certifications.",
            "Use action verbs like Developed, Built, Designed."
        ]

    return suggestions, missing_skills