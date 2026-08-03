import re

def compare_resume_job(resume_text, job_description):

    resume = resume_text.lower()
    job = job_description.lower()

    words = re.findall(r"\b[a-zA-Z]+\b", job)

    keywords = list(set(words))

    matched = []
    missing = []

    for word in keywords:

        if len(word) < 3:
            continue

        if word in resume:
            matched.append(word)

        else:
            missing.append(word)

    if len(keywords) == 0:
        score = 0

    else:
        score = int((len(matched) / len(keywords)) * 100)

    return score, matched, missing