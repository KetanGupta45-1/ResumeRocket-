from PyPDF2 import PdfReader

def extract_text(pdf_path):
    pdf = PdfReader(pdf_path)
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "


    return text.strip()
