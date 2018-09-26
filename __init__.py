# s3Uploader/__init__.py

from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from .helpers import upload_file_to_s3

app     = Flask(__name__)
app.config.from_envvar('APPSETTINGS')

ALLOWED_EXTENSIONS = set(['mp4'])

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["POST"])
def upload_file():

	# A
    if "user_file" not in request.files:
        return "No user_file key in request.files"

	# B
    file    = request.files["user_file"]

    """
        These attributes are also available

        file.filename               # The actual name of the file
        file.content_type
        file.content_length
        file.mimetype

    """

	# C.
    if file.filename == "":
        return "Please select a file"

	# D.
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output   	  = upload_file_to_s3(file, app.config["S3_BUCKET"])
        return str(output)

    else:
        return redirect("/")