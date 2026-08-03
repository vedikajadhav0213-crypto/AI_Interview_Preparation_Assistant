from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_certificate(name, score, filename):

    c = canvas.Canvas(filename, pagesize=A4)

    width, height = A4

    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width/2, 760, "Certificate of Completion")

    c.setFont("Helvetica", 18)
    c.drawCentredString(
        width/2,
        690,
        "This certificate is awarded to"
    )

    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, 650, name)

    c.setFont("Helvetica", 18)
    c.drawCentredString(
        width/2,
        600,
        f"Interview Score : {score}%"
    )

    c.drawCentredString(
        width/2,
        560,
        "AI Interview Preparation Assistant"
    )

    c.save()