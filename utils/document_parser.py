from docx import Document

def extract_candidate_info(doc_path):
    doc = Document(doc_path)
    full_text = ""
    
    # Iterate through all paragraphs and concatenate them into a single string
    for para in doc.paragraphs:
        full_text += para.text + "\n"  # Adding newline for better formatting
    
    return full_text.strip()  # Return the full text as a single string
