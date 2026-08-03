def generate_questions(skills):

    question_bank = {

        "Python": [
            "What is Python?",
            "Explain List and Tuple.",
            "What are Python decorators?",
            "What is a lambda function?",
            "Explain generators in Python.",
            "What is inheritance?",
            "What is polymorphism?",
            "Difference between List and Dictionary.",
            "What is exception handling?",
            "What are Python modules and packages?"
        ],

        "SQL": [
        "What is SQL?",
        "Explain INNER JOIN.",
        "What is Primary Key?",
        "Difference between DELETE and TRUNCATE.",
        "Difference between DELETE and DROP.",
        "Explain LEFT JOIN.",
        "What is Normalization?",
        "Difference between WHERE and HAVING.",
        "Explain GROUP BY.",
        "What are Indexes?"
    ],


        "Flask": [
            "What is Flask?",
            "Explain Flask Routing.",
            "What is Jinja2?",
            "What is Flask Session?",
            "Explain Blueprints.",
            "What is request object?",
            "Difference between GET and POST.",
            "How do you connect Flask with SQLite?",
            "How does Flask render HTML templates?",
            "What is url_for()?"
        ],

        "Machine Learning": [
           "What is Machine Learning?",
            "Difference between Supervised and Unsupervised Learning.",
            "Explain Overfitting.",
            "What is Underfitting?",
            "What is Cross Validation?",
            "Difference between Classification and Regression.",
            "Explain Decision Tree.",
            "What is Random Forest?",
            "What is KNN?",
            "What is Linear Regression?"
        ],

          "HTML": [
        "What is HTML?",
        "Difference between div and span.",
        "What are semantic tags?",
        "Difference between id and class.",
        "What is the purpose of forms?",
        "What is the use of meta tag?",
        "Difference between block and inline elements?",
        "What is an iframe?"
    ],

    "CSS": [
        "What is CSS?",
        "Explain Flexbox.",
        "What is Grid Layout?",
        "Difference between margin and padding.",
        "What is z-index?",
        "What is media query?",
        "Explain position properties.",
        "Difference between inline, internal and external CSS."
    ],

    "JavaScript": [
        "What is JavaScript?",
        "Difference between var, let and const.",
        "What is DOM?",
        "What are arrow functions?",
        "Explain promises.",
        "What is async and await?",
        "Difference between == and ===.",
        "What are events in JavaScript?",
        "What is event bubbling?",
        "What is JSON?"
    ],

    "Git": [
        "What is Git?",
        "Difference between Git and GitHub.",
        "What is a branch?",
        "What is merge?",
        "Explain git clone.",
        "Explain git pull.",
        "Explain git push.",
        "What is git commit?"
    ],

"GitHub": [
    "What is GitHub?",
    "Difference between Git and GitHub.",
    "What is a Fork in GitHub?",
    "What is a Pull Request?",
    "What is a Branch?",
    "How do you resolve merge conflicts?",
    "What is GitHub Actions?",
    "What is a Repository?",
    "What is README.md?",
    "How do you collaborate using GitHub?"
],

"Docker": [
    "What is Docker?",
    "Why is Docker used?",
    "Difference between Docker Image and Container.",
    "What is Dockerfile?",
    "What is Docker Compose?",
    "What is Docker Hub?",
    "How do you create a Docker image?",
    "How do you run a Docker container?",
    "Explain docker build command.",
    "Explain docker run command."
],

"AWS": [
    "What is AWS?",
    "What are the advantages of AWS?",
    "What is Amazon EC2?",
    "What is Amazon S3?",
    "What is AWS Lambda?",
    "What is IAM in AWS?",
    "What is Amazon RDS?",
    "Difference between EC2 and Lambda.",
    "What is Elastic Beanstalk?",
    "What is CloudWatch?"
],

"OOP": [
    "What is Object-Oriented Programming?",
    "What are the four pillars of OOP?",
    "Explain Encapsulation.",
    "Explain Inheritance.",
    "Explain Polymorphism.",
    "Explain Abstraction.",
    "Difference between Method Overloading and Overriding.",
    "What is a Constructor?",
    "What is a Class?",
    "What is an Object?"
],

"DBMS": [
    "What is DBMS?",
    "Difference between DBMS and RDBMS.",
    "What is Normalization?",
    "What are ACID properties?",
    "What is a Primary Key?",
    "What is a Foreign Key?",
    "What is a Candidate Key?",
    "What is an Index?",
    "Difference between DELETE, DROP and TRUNCATE.",
    "Explain SQL Joins."
]

}
        

    questions = []

    for skill in skills:

        if skill in question_bank:

            questions.extend(question_bank[skill])

    return questions[:5]