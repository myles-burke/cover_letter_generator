from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
import shutil
from aiCall import sendMessage

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "data")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/upload", methods=["POST"])
def upload():
    print("Active")
    try:
        resume = request.files.get("resume")
        job = request.files.get("job")

        if not resume or not job or resume.filename == "" or job.filename == "":
            return jsonify(success=False, error="Missing file"), 400

        resume.save(os.path.join(UPLOAD_FOLDER, secure_filename(resume.filename)))
        job.save(os.path.join(UPLOAD_FOLDER, secure_filename(job.filename)))

        # Logic
        text = "describe earth"
        response = sendMessage (text)
        return jsonify(success=True, message=response)

    except Exception as e:
        print("UPLOAD ERROR:", e)
        return jsonify(success=False, error=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
    # Clean folder
