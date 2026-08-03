from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_report(name, ats_score, interview_score, skills, feedback):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{name}_Interview_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Interview Preparation Assistant</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Name:</b> {name}", styles["BodyText"]))
    story.append(Paragraph(f"<b>ATS Score:</b> {ats_score}%", styles["BodyText"]))
    story.append(Paragraph(f"<b>Interview Score:</b> {interview_score}%", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Skills</b>", styles["Heading2"]))

    for skill in skills:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Feedback</b>", styles["Heading2"]))

    for item in feedback:
        story.append(Paragraph(f"• {item}", styles["BodyText"]))

    doc.build(story)

    return filename