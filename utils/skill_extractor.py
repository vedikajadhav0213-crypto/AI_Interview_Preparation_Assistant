def extract_skills(resume_text):

    skills_list = [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Flask",
        "Django",
        "React",
        "Node.js",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "Power BI",
        "Excel",
        "Git",
        "GitHub",
        "TensorFlow",
        "PyTorch",
        "NLP",
        "Pandas",
        "NumPy",
        "Scikit-learn"
    ]

    found_skills = []

    resume_text = resume_text.lower()

    for skill in skills_list:
        if skill.lower() in resume_text:
            found_skills.append(skill)

    return found_skills