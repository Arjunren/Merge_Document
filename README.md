# Merge_Document
A professional Python-based CLI utility for merging PDF and DOCX documents. Features robust handling of document streams and automated page-break insertion for Word files to ensure structural integrity across combined assets.

# 📄 DocMerge CLI: Professional Document Consolidation

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PyPDF2](https://img.shields.io/badge/Library-PyPDF2-blue)](https://pypdf2.readthedocs.io/)
[![python-docx](https://img.shields.io/badge/Library-python--docx-green)](https://python-docx.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**DocMerge CLI** is a robust command-line utility designed to simplify the process of merging multiple PDF and Microsoft Word (DOCX) documents. Whether you are compiling reports, legal documents, or academic papers, this tool provides a fast and reliable way to consolidate your files into a single, cohesive output.

---

## ✨ Key Features

### 📑 Multi-Format Support
* **PDF Merging:** Utilizes `PdfMerger` to combine any number of PDF files while preserving document order and internal metadata.
* **DOCX Merging:** Seamlessly appends multiple Word documents, maintaining element structures (paragraphs, tables, images).

### 📐 Structural Integrity
* **Automated Page Breaks:** When merging Word documents, the tool automatically inserts page breaks between files to ensure the content of each document starts on a fresh page.
* **Interactive Interface:** A simple, prompt-based CLI that guides you through file selection and output naming.

### ⚡ Performance
* **Streamlined Processing:** Leverages memory-efficient libraries to handle large document sets without significant overhead.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher.
* The following Python packages: `PyPDF2`, `python-docx`.

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Arjunren/Merge_Document
    cd Merge_Document
    ```

2.  **Install dependencies:**
    ```bash
    pip install PyPDF2 python-docx
    ```

3.  **Run the tool:**
    ```bash
    python app.py
    ```

---

## 📖 Usage Guide

Upon launching the script, follow the interactive prompts:

1.  **Choose Type:** Enter `1` for PDF or `2` for DOCX.
2.  **Input Files:** Provide the paths to your files, separated by commas.
    * *Example:* `doc1.pdf, doc2.pdf, doc3.pdf`
3.  **Output Name:** Enter the desired filename for the merged result (e.g., `Final_Report.pdf`).

---

## 🧪 Technical Implementation

The tool follows a professional document-processing pipeline:
* **PDF Logic:** Uses `merger.append()` for each file path, followed by a consolidated write operation to minimize file system I/O.
* **DOCX Logic:** Iterates through the XML body of each document, appending elements to a master `merged_document` object.
* **Path Handling:** Implements automatic string stripping to handle spaces in comma-separated user inputs.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed for efficient document workflows and administrative automation.**
