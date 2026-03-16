from pdfminer.high_level import extract_text
from docx import Document


def extract_text_from_file(file):

    filename = file.filename.lower()

    # PDF
    if filename.endswith(".pdf"):
        return extract_text(file.file)

    # Word
    elif filename.endswith(".docx"):
        doc = Document(file.file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text

    # TXT
    elif filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

    else:
        raise ValueError("Unsupported file format")