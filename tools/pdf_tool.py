import PyPDF2
from typing import Dict

def summarize_pdf(input_path: str) -> Dict:
    """
    Very basic PDF text extraction and naive summary (first ~800 chars).
    input_path: path to pdf
    """
    reader = PyPDF2.PdfReader(input_path)
    pages_text = []
    for p in reader.pages:
        text = p.extract_text()
        if text:
            pages_text.append(text)
    full = "\n".join(pages_text)
    return {"text_excerpt": full[:2000], "length": len(full)}
