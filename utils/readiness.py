def predict_readiness(ats_score, interview_score):

    overall = (ats_score + interview_score) / 2

    if overall >= 85:

        status = "Ready for Interviews ✅"

        advice = [
            "Start applying for jobs.",
            "Keep practicing advanced interview questions.",
            "Update your resume regularly."
        ]

    elif overall >= 65:

        status = "Almost Ready 🟡"

        advice = [
            "Practice more mock interviews.",
            "Improve communication skills.",
            "Strengthen weak technical areas."
        ]

    else:

        status = "Needs More Practice 🔴"

        advice = [
            "Improve your resume.",
            "Study core programming concepts.",
            "Practice coding daily.",
            "Take more mock interviews."
        ]

    return status, advice