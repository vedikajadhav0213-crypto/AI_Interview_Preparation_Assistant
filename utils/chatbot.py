def get_bot_response(question):

    question = question.lower()

    responses = {

        "python": "Python is a high-level, interpreted programming language used for web development, AI, data science, automation, and more.",

        "sql": "SQL (Structured Query Language) is used to create, retrieve, update, and manage data stored in relational databases.",

        "flask": "Flask is a lightweight Python web framework used to build web applications and REST APIs.",

        "machine learning": "Machine Learning is a branch of AI where computers learn patterns from data to make predictions or decisions.",

        "oop": "Object-Oriented Programming is based on classes and objects. Its main principles are Encapsulation, Inheritance, Polymorphism, and Abstraction.",

        "list": "A List is mutable, while a Tuple is immutable in Python.",

        "tuple": "A Tuple is immutable and generally faster than a List.",

        "numpy": "NumPy is a Python library used for numerical computing.",

        "pandas": "Pandas is used for data analysis and data manipulation.",

        "html": "HTML is used to create web pages.",

        "css": "CSS is used to style web pages.",

        "javascript": "JavaScript makes web pages interactive.",

        "nlp": "NLP (Natural Language Processing) is a branch of Artificial Intelligence that enables computers to understand, interpret, and generate human language.",

        "resume": "A good resume should include skills, projects, education, internships, certifications, and measurable achievements.",

        "interview": "Stay confident, communicate clearly, explain your approach, and support your answers with examples."

    }

    for key in responses:
        if key in question:
            return responses[key]

    return "Sorry, I don't have an answer for that. Please try another interview-related question."
    return "Sorry, I don't have an answer for that. Please try another interview-related question."