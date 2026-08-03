import re

def recommend_keywords(resume_text, job_description):

    resume = resume_text.lower()

    words = re.findall(r"[a-zA-Z][a-zA-Z+#.]*", job_description.lower())

    stop_words = {
        "the", "and", "for", "with", "you", "your", "this", "that",
        "are", "will", "our", "have", "has", "from", "into",
        "job", "role", "candidate", "experience", "years"
    }

    keywords = sorted(set(words))

    recommendations = []

    for word in keywords:

        if len(word) < 3:
            continue

        if word in stop_words:
            continue

        if word not in resume:
            recommendations.append(word.title())

    return recommendations