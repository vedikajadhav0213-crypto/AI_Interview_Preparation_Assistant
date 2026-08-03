import os
import sqlite3
from utils.resume_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from werkzeug.utils import secure_filename
from utils.answer_evaluator import evaluate_answer
from utils.pdf_generator import generate_report
from utils.resume_feedback import get_resume_feedback
from utils.chatbot import get_bot_response
from utils.job_recommender import recommend_jobs
from utils.resume_improvement import get_resume_improvements
from utils.question_generator import generate_questions
from utils.certificate import generate_certificate
from utils.resume_improver import get_resume_suggestions
from utils.job_match import compare_resume_job
from utils.performance_analysis import analyze_performance
from utils.readiness import predict_readiness
from utils.keyword_optimizer import recommend_keywords
from utils.certificate_generator import generate_certificate
from flask import send_file

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from werkzeug.utils import secure_filename

from utils.resume_parser import extract_text
from utils.skill_extractor import extract_skills


# ---------------------------------------------------
# Flask App
# ---------------------------------------------------

app = Flask(__name__)
from flask_mail import Mail, Message

app.secret_key = "your_secret_key"
# -----------------------------
# Email Configuration
# -----------------------------

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "vedikajadhav0213@gmail.com"
app.config["MAIL_PASSWORD"] = "vedika2637"

mail = Mail(app)

DATABASE = "database.db"

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------------------------------------------
# Database Connection
# ---------------------------------------------------

def get_db_connection():

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


# ---------------------------------------------------
# Home
# ---------------------------------------------------

@app.route("/")
def home():

    return render_template("index.html")


# ---------------------------------------------------
# Register
# ---------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()

        try:

            conn.execute(
                "INSERT INTO users(name,email,password) VALUES(?,?,?)",
                (name, email, hashed_password)
            )

            conn.commit()

            flash("Registration Successful!")

            return redirect(url_for("login"))

        except sqlite3.IntegrityError:

            flash("Email already exists!")

        finally:

            conn.close()

    return render_template("register.html")


# ---------------------------------------------------
# Login
# ---------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        conn.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["user_name"] = user["name"]

            flash("Login Successful!")

            return redirect(url_for("dashboard"))

        else:

            flash("Invalid Email or Password")

    return render_template("login.html")


# ---------------------------------------------------
# Dashboard
# ---------------------------------------------------

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    ats_score = session.get("ats_score", 0)
    interview_score = session.get("interview_score", 0)
    skills_count = session.get("skills_count", 0)

    if interview_score >= 90:
        performance = "Excellent"

    elif interview_score >= 70:
        performance = "Good"

    elif interview_score >= 50:
        performance = "Average"

    else:
        performance = "Needs Improvement"

    return render_template(
        "dashboard.html",
        name=session["user_name"],
        ats_score=ats_score,
        interview_score=interview_score,
        skills_count=skills_count,
        performance=performance
    )

# ---------------------------------------------------
# Dashboard Analytics
# ---------------------------------------------------

@app.route("/analytics")
def analytics():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    total_users = conn.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    total_interviews = conn.execute(
        "SELECT COUNT(*) FROM interview_history"
    ).fetchone()[0]

    average_score = conn.execute(
        "SELECT AVG(interview_score) FROM interview_history"
    ).fetchone()[0]

    if average_score is None:
        average_score = 0

    history = conn.execute(
        """
        SELECT interview_date, interview_score
        FROM interview_history
        WHERE user_id=?
        ORDER BY id
        """,
        (session["user_id"],)
    ).fetchall()

    conn.close()

    dates = [row["interview_date"] for row in history]
    scores = [row["interview_score"] for row in history]

    return render_template(
        "analytics.html",
        total_users=total_users,
        total_interviews=total_interviews,
        average_score=round(average_score, 2),
        dates=dates,
        scores=scores
    )

@app.route("/profile", methods=["GET", "POST"])
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    if request.method == "POST":

        name = request.form["username"]

        conn.execute(
            "UPDATE users SET name=? WHERE id=?",
            (name, session["user_id"])
        )

        conn.commit()

        session["user_name"] = name

        return redirect(url_for("dashboard"))

    conn.close()

    return render_template(
        "profile.html",
        user=user
    )

# ---------------------------------------------------
# Upload Resume
# ---------------------------------------------------

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        if "resume" not in request.files:
            flash("Please select a file.")
            return redirect(request.url)

        file = request.files["resume"]

        if file.filename == "":
            flash("Please select a file.")
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        file.save(filepath)
        try:
            # Parse Resume
            resume_text = extract_text(filepath)
            resume_text = extract_text(filepath)
            suggestions = get_resume_suggestions(resume_text)

            session["resume_suggestions"] = suggestions

            print("\n========== RESUME TEXT ==========\n")
            print(resume_text)
            print("\n=================================\n")

            # Extract Skills
            skills = extract_skills(resume_text)

            print("\n========== SKILLS FOUND ==========\n")
            print(skills)
            print("\n==================================\n")

            # Calculate ATS Score
            ats_score = calculate_ats_score(resume_text, skills)
            session["ats_score"] = ats_score
            improvements = get_resume_improvements(ats_score, skills)

            session["resume_improvements"] = improvements
            session["skills"] = skills
            questions = generate_questions(skills)

            session["generated_questions"] = questions
            session["skills_count"] = len(skills)
            # Save ATS Score
            session["ats_score"] = ats_score

            print("\n========== ATS SCORE ==========\n")
            print("ATS Score:", ats_score)
            print("\n===============================\n")

            flash(f"Resume uploaded successfully! ATS Score: {ats_score}")

        except Exception as e:

            print("Resume Parser Error:", e)

            flash("Resume uploaded, but parsing failed.")

        return redirect(url_for("dashboard"))

    return render_template("upload.html")


# ---------------------------------------------------
# ATS Score
# ---------------------------------------------------
# ---------------------------------------------------
# ATS Score Page
# ---------------------------------------------------

@app.route("/ats")
def ats():

    if "user_id" not in session:
        return redirect (url_for("login"))

    ats_score = session.get("ats_score", 0)
    resume_text = session.get("resume_text", "")

    suggestions, missing_skills = get_resume_feedback(
        ats_score,
        resume_text
    )

    return render_template(
    "ats.html",
    ats_score=ats_score,
    skills=session.get("skills", []),
    suggestions=suggestions,
    missing_skills=missing_skills,
    resume_suggestions=session.get("resume_suggestions", [])
)

@app.route("/job_match", methods=["GET", "POST"])
def job_match():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        job_description = request.form["job_description"]

        resume_text = session.get("resume_text", "")

        score, matched, missing = compare_resume_job(
            resume_text,
            job_description
        )
        recommended_keywords = recommend_keywords(
            resume_text,
            job_description
        )

        return render_template(
            "job_match.html",
            score=score,
            matched=matched,
            missing=missing,
            recommended_keywords=recommended_keywords
        )

    return render_template("job_match.html")

# ---------------------------------------------------
# Mock Interview
# ---------------------------------------------------

@app.route("/mock_interview", methods=["GET", "POST"])
def mock_interview():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    generated_questions = session.get("generated_questions", [])

    questions = []

    for i, q in enumerate(generated_questions):

     questions.append({
        "id": i + 1,
        "question": q,
        "answer": ""
    })

    if request.method == "POST":

        score = 0
        total = len(questions)

        for question in questions:

            user_answer = request.form.get(
                f"answer{question['id']}",
                ""
            )

            correct_answer = question["answer"]

            print("--------------------------------")
            print("Question:", question["question"])
            print("Correct Answer:", correct_answer)
            print("User Answer:", user_answer)

            if user_answer.strip() != "":
             score += 1

        percentage = int((score / total) * 100)

        print("Correct:", score)
        print("Total:", total)
        print("Percentage:", percentage)

        session["interview_score"] = percentage
        from datetime import datetime

        conn.execute(
        """
        INSERT INTO interview_history
        (user_id, interview_score, ats_score, interview_date)
        VALUES (?, ?, ?, ?)
        """,
        (
        session["user_id"],
        percentage,
        session.get("ats_score", 0),
        datetime.now().strftime("%d-%m-%Y %H:%M")
    )
)

        conn.commit()
        conn.close()

        return redirect(url_for("result"))

    conn.close()

    return render_template(
        "mock_interview.html",
        questions=questions
    )

# ---------------------------------------------------
# Interview Result
# ---------------------------------------------------

@app.route("/result")
def result():

    if "user_id" not in session:
        return redirect(url_for("login"))

    score = session.get("interview_score", 0)
    ats_score = session.get("ats_score", 0)

    status, advice = predict_readiness(
    ats_score,
    score
)
    strengths, weaknesses, tips, rating = analyze_performance(score)

    if score >= 90:
        performance = "Excellent"
        feedback = [
            "Excellent technical knowledge.",
            "Your communication is very good.",
            "You are ready for technical interviews."
        ]

    elif score >= 70:
        performance = "Good"
        feedback = [
            "Good performance overall.",
            "Practice more coding questions.",
            "Improve confidence while answering."
        ]

    elif score >= 50:
        performance = "Average"
        feedback = [
            "Basic concepts are clear.",
            "Revise Python and SQL.",
            "Practice mock interviews regularly."
        ]

    else:
        performance = "Needs Improvement"
        feedback = [
            "Improve programming fundamentals.",
            "Practice SQL queries.",
            "Improve communication skills.",
            "Solve more interview questions."
        ]

    name = session.get("user_name")
    ats_score = session.get("ats_score", 0)
    skills = session.get("skills", [])

    pdf_path = generate_report(
        name,
        ats_score,
        score,
        skills,
        feedback
    )

    session["pdf_path"] = pdf_path

    return render_template(
    "result.html",
    score=score,
    performance=performance,
    feedback=feedback,
    strengths=strengths,
    weaknesses=weaknesses,
    tips=tips,
    rating=rating,
    status=status,
    advice=advice
)

from flask import send_file


@app.route("/download_report")
def download_report():

    if "user_id" not in session:
        return redirect(url_for("login"))

    pdf = session.get("pdf_path")

    return send_file(pdf, as_attachment=True)

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    if "user_id" not in session:
        return redirect(url_for("login"))

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        answer = get_bot_response(question)

    return render_template(
        "chatbot.html",
        answer=answer
    )

@app.route("/certificate")
def certificate():

    if "user_id" not in session:
        return redirect(url_for("login"))

    name = session.get("user_name", "User")
    score = session.get("interview_score", 0)

    filename = "static/certificate.pdf"

    generate_certificate(
        name,
        score,
        filename
    )

    return send_file(
        filename,
        as_attachment=True
    )

# ---------------------------------------------------
# Voice Interview
# ---------------------------------------------------

@app.route("/voice_interview")
def voice_interview():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("voice_interview.html")

# ---------------------------------------------------
# Interview History
# ---------------------------------------------------

@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    history = conn.execute(
        """
        SELECT *
        FROM interview_history
        WHERE user_id=?
        ORDER BY id DESC
        """,
        (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template(
        "history.html",
        history=history
    )

@app.route("/certificate")
def certificate():

    if "user_id" not in session:
        return redirect(url_for("login"))

    generate_certificate(
        session["user_name"],
        session.get("interview_score", 0),
        session.get("performance", "Good")
    )

    return send_file(
        "reports/certificate.pdf",
        as_attachment=True
    )

# ---------------------------------------------------
# Job Recommendation
# ---------------------------------------------------

@app.route("/jobs")
def jobs():

    if "user_id" not in session:
        return redirect(url_for("login"))

    ats_score = session.get("ats_score", 0)
    interview_score = session.get("interview_score", 0)

    jobs = recommend_jobs(
        ats_score,
        interview_score
    )

    return render_template(
        "jobs.html",
        jobs=jobs,
        ats_score=ats_score,
        interview_score=interview_score
    )

# ---------------------------------------------------
# Admin Panel
# ---------------------------------------------------

@app.route("/admin")
def admin():

    conn = get_db_connection()

    users = conn.execute("""
        SELECT
            users.id,
            users.name,
            users.email,
            interview_history.ats_score,
            interview_history.interview_score,
            interview_history.interview_date
        FROM users

        LEFT JOIN interview_history

        ON users.id = interview_history.user_id

        ORDER BY users.id ASC
    """).fetchall()

    conn.close()

    return render_template(
        "admin.html",
        users=users
    )
@app.route("/send_email")
def send_email():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    conn.close()

    ats = session.get("ats_score", 0)
    interview = session.get("interview_score", 0)

    msg = Message(
        subject="AI Interview Report",
        sender=app.config["MAIL_USERNAME"],
        recipients=[user["email"]]
    )

    msg.body = f"""
Hello {user['name']},

Your AI Interview Report

ATS Score : {ats}%

Interview Score : {interview}%

Thank you for using AI Interview Preparation Assistant.

Best Wishes!
"""

    mail.send(msg)

    flash("Email sent successfully!")

    return redirect(url_for("result"))
# ---------------------------------------------------
# Logout
# ---------------------------------------------------

@app.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully")

    return redirect(url_for("home"))


# ---------------------------------------------------
# Run Application
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )