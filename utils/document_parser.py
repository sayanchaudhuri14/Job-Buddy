import os
import fitz  # PyMuPDF for PDF processing
from docx import Document
import streamlit as st

def extract_candidate_info(uploaded_file):
    """Extract text from an uploaded resume file (PDF or DOCX)."""
    if uploaded_file is None:
        raise ValueError("No file uploaded.")

    file_ext = os.path.splitext(uploaded_file.name)[-1].lower()

    if file_ext == ".docx":
        return extract_text_from_docx(uploaded_file)
    elif file_ext == ".pdf":
        return extract_text_from_pdf(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please provide a .docx or .pdf file.")

def extract_text_from_docx(uploaded_file):
    """Extract text from a DOCX file."""
    doc = Document(uploaded_file)
    return "\n".join(para.text for para in doc.paragraphs).strip()

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file."""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = "\n".join(page.get_text("text") for page in doc)
    return text.strip()
