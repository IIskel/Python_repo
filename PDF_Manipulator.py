#Install requirements
#pip install PyPDF2, PyMuPDF, Pillow, opencv-python
import fitz  # type: ignore # PyMuPDF for handling PDFs
from PIL import Image # type: ignore
import io

#Extract text from PDF
def extract_text_from_pdf(pdf_path):
    """Extract text from each page of the PDF."""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf[page_num]
            text = page.get_text()
            # if "pyth" in text:
            #   print("yes")
            print(f"Page {page_num + 1} Text:\n{text}\n")
            print("-" * 50)
pdf_file_path = "/content/GE8151-PYTHON.pdf"
output_folder_path = "/content/sample_data"  # Ensure this folder exists

# Extract text from the PDF
extract_text_from_pdf(pdf_file_path)

#Scan PDF
def scan_pdf_pages(pdf_path, output_folder):
    """Scan each page as an image and save it."""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf[page_num]
            # Render the page as a PNG image
            pix = page.get_pixmap()
            # Save the image for inspection, Using save() method and specifying output format
            output_path = f"{output_folder}/page_{page_num + 1}.png"
            pix.save(output_path)  # Directly save the pixmap
            print(f"Saved page {page_num + 1} as an image at {output_path}")

scan_pdf_pages(pdf_file_path, output_folder_path)