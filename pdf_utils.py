import io
from fpdf import FPDF
from PyPDF2 import PdfReader

def save_to_pdf(data: dict, filename: str) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, data['title'], ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 10)
    
    for line in data['content'].split('\n'):
        pdf.multi_cell(0, 10, line)
    
    pdf.output(filename)

def process_pdf_file(pdf_file) -> str:
    text = ""
    pdf_reader = PdfReader(pdf_file)
    
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text() + "\n"
    
    return text.strip()
