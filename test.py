from reportlab.lib.pagesizes import letter
import os
import json
from tkinter import Tk, filedialog
from parser.utils import extract_text, parse_resume, save_to_word

def select_resume_file():
    Tk().withdraw()  # Hide root window
    file_path = filedialog.askopenfilename(
        title="Select Resume PDF",
        filetypes=[("PDF files", "*.pdf")]
    )
    return file_path

def main():
    print("📄 AI Resume Parser\n")

    file_path = select_resume_file()
    if not file_path:
        print("❌ No file selected.")
        return

    print("🔍 Extracting text from:", file_path)
    text = extract_text(file_path)

    print("🧠 Parsing resume...")
    parsed_data = parse_resume(text)

    print("\n✅ Parsed Resume Data:\n")
    print(json.dumps(parsed_data, indent=2))

    output_docx = "parsed_resume.docx"
    save_to_word(parsed_data, output_path=output_docx)
    print(f"\n📁 Word document saved as: {output_docx}")

    # ✅ Open the Word file automatically
    os.startfile(output_docx)

if __name__ == "__main__":
    main()
