def recommend_jobs(ats_score, interview_score):

    jobs = []

    average = (ats_score + interview_score) / 2

    if average >= 90:

        jobs = [
            "Machine Learning Engineer",
            "AI Engineer",
            "Data Scientist",
            "Software Development Engineer",
            "Backend Python Developer"
        ]

    elif average >= 75:

        jobs = [
            "Python Developer",
            "Data Analyst",
            "Web Developer",
            "Software Engineer",
            "QA Automation Engineer"
        ]

    elif average >= 60:

        jobs = [
            "Junior Python Developer",
            "Technical Support Engineer",
            "SQL Developer",
            "Frontend Developer",
            "Testing Engineer"
        ]

    else:

        jobs = [
            "Improve Resume",
            "Practice Mock Interviews",
            "Learn Python",
            "Complete Projects",
            "Apply for Internships"
        ]

    return jobs