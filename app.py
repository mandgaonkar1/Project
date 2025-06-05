from flask import Flask, render_template, request, jsonify
from parser.utils import extract_text, parse_resume
from flask import Flask, render_template, request, send_file
from parser.utils import extract_text, parse_resume, save_to_word
import json
from flask import Flask, render_template, request, send_file
from parser.utils import extract_text, parse_resume, save_to_word
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    parsed_data = None
    download_link = None

    if request.method == 'POST':
        uploaded_file = request.files['resume']
        if uploaded_file and uploaded_file.filename.endswith('.pdf'):
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)

            text = extract_text(filepath)
            parsed_data = parse_resume(text)

            output_path = os.path.join("outputs", "parsed_resume.docx")
            os.makedirs("outputs", exist_ok=True)
            save_to_word(parsed_data, output_path)

            download_link = "/download"

    return render_template('index.html', data=parsed_data, download_link=download_link)

@app.route('/download')
def download_file():
    return send_file("outputs/parsed_resume.docx", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
