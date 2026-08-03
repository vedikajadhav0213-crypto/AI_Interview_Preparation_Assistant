def get_resume_suggestions(resume_text):

    suggestions = []

    text = resume_text.lower()

    if "github" not in text:
        suggestions.append("Add your GitHub profile link.")

    if "linkedin" not in text:
        suggestions.append("Add your LinkedIn profile.")

    if "project" not in text:
        suggestions.append("Mention your academic or personal projects.")

    if "certification" not in text:
        suggestions.append("Include relevant certifications.")

    if "python" not in text:
        suggestions.append("Mention your programming skills.")

    if len(suggestions) == 0:
        suggestions.append("Excellent Resume! No major improvements needed.")

    return suggestions