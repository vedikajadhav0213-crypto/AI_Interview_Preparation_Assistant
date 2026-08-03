import pdfplumber
from docx import Document

def extract_text(file_path):

    text = ""

    if file_path.lower().endswith(".pdf"):

        with pdfplumber.open(file_path) as pdf:

            # Read only first 5 pages
            for page in pdf.pages[:5]:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    elif file_path.lower().endswith(".docx"):

        doc = Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    return text