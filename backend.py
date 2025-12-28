# pip install flask werkzeug
from flask import Flask, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return open("main.html").read()


@app.route("/data", methods=["POST"])
def upload():
    resume = request.files.get("resume")
    job = request.files.get("job")

    if not resume or not job or resume.filename == "" or job.filename == "":
        return redirect("/?error=1")

    resume.save(os.path.join(UPLOAD_FOLDER, secure_filename(resume.filename)))
    job.save(os.path.join(UPLOAD_FOLDER, secure_filename(job.filename)))

    return "Files uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)
