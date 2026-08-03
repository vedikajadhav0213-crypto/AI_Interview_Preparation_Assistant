def analyze_performance(score):

    strengths = []
    weaknesses = []
    tips = []

    if score >= 90:

        strengths = [
            "Excellent technical knowledge",
            "Strong communication",
            "Very confident answers"
        ]

        tips = [
            "Keep practicing regularly.",
            "Apply for advanced roles."
        ]

        rating = "Excellent ⭐⭐⭐⭐⭐"

    elif score >= 70:

        strengths = [
            "Good understanding of concepts",
            "Answered most questions correctly"
        ]

        weaknesses = [
            "Some answers need more detail",
            "Confidence can be improved"
        ]

        tips = [
            "Practice mock interviews.",
            "Improve communication skills."
        ]

        rating = "Good ⭐⭐⭐⭐"

    else:

        weaknesses = [
            "Need stronger technical knowledge",
            "Low confidence",
            "Short answers"
        ]

        tips = [
            "Study core subjects.",
            "Practice coding daily.",
            "Take more mock interviews."
        ]

        rating = "Needs Improvement ⭐⭐"

    return strengths, weaknesses, tips, rating