from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_certificate(name, score, performance):

    pdf = SimpleDocTemplate("reports/certificate.pdf")

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b><font size=24>Certificate of Completion</font></b>", styles["Title"]))

    story.append(Paragraph("<br/><br/>", styles["Normal"]))

    story.append(Paragraph(f"<font size=18>This certifies that</font>", styles["Heading2"]))

    story.append(Paragraph(f"<font size=22><b>{name}</b></font>", styles["Title"]))

    story.append(Paragraph("<br/>has successfully completed the AI Mock Interview.</br>", styles["Heading2"]))

    story.append(Paragraph(f"Interview Score : <b>{score}%</b>", styles["Heading2"]))

    story.append(Paragraph(f"Performance : <b>{performance}</b>", styles["Heading2"]))

    pdf.build(story)