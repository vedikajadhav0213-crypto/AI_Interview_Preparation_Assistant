def get_resume_improvements(ats_score, skills):

    suggestions = []

    if ats_score >= 90:
        suggestions = [
            "Excellent resume.",
            "Keep your resume updated regularly.",
            "Add your latest projects.",
            "Customize your resume for every job application."
        ]

    elif ats_score >= 70:
        suggestions = [
            "Add more technical skills.",
            "Include relevant certifications.",
            "Improve your project descriptions.",
            "Mention measurable achievements.",
            "Add your GitHub profile."
        ]

    else:
        suggestions = [
            "Improve resume formatting.",
            "Add more technical skills.",
            "Include internships or projects.",
            "Use ATS keywords.",
            "Add certifications.",
            "Include GitHub and LinkedIn profile.",
            "Use action verbs like Developed, Built, Designed."
        ]

    # Skill-based suggestions
    important_skills = [
        "Python",
        "SQL",
        "Flask",
        "Machine Learning",
        "HTML",
        "CSS",
        "JavaScript",
        "Git"
    ]

    for skill in important_skills:
        if skill not in skills:
            suggestions.append(f"Consider adding {skill} if you have experience.")

    return suggestions