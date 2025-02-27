import PyPDF2
import docx

def extract_text_from_resume(file):
    """Extract text from PDF or DOCX resumes."""
    text = ""
    if file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        text = " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        text = " ".join([para.text for para in doc.paragraphs])
    return text
