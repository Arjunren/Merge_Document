import os
from PyPDF2 import PdfMerger
from docx import Document

def merge_pdfs(pdf_files, output_file):
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()
    print(f"Merged PDF saved as: {output_file}")


def merge_docx(docx_files, output_file):
    merged_document = Document()

    for i, file in enumerate(docx_files):
        doc = Document(file)

        for element in doc.element.body:
            merged_document.element.body.append(element)

        # Add page break between documents (except last)
        if i != len(docx_files) - 1:
            merged_document.add_page_break()

    merged_document.save(output_file)
    print(f"Merged DOCX saved as: {output_file}")


if __name__ == "__main__":
    print("Choose file type to merge:")
    print("1. PDF")
    print("2. DOCX")

    choice = input("Enter choice (1 or 2): ")

    files = input("Enter file paths separated by commas:\n").split(",")
    files = [f.strip() for f in files]

    output = input("Enter output file name (with extension): ")

    if choice == "1":
        merge_pdfs(files, output)
    elif choice == "2":
        merge_docx(files, output)
    else:
        print("Invalid choice.")