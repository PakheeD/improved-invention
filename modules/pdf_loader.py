from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text += page_text
        return text.strip()
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"
