# pip install flask werkzeug
from flask import Flask, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "data")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/upload", methods=["POST"])
def upload():
    resume = request.files.get("resume")
    job = request.files.get("job")

    if not resume or not job or resume.filename == "" or job.filename == "":
        return {"success": False, "error": "Missing file"}, 400

    resume.save(os.path.join(UPLOAD_FOLDER, secure_filename(resume.filename)))
    job.save(os.path.join(UPLOAD_FOLDER, secure_filename(job.filename)))

    return {"success": True}

if __name__ == "__main__":
    app.run(debug=True)
