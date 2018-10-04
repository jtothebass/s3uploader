# s3uploader/app.py

from flask import Flask, flash, request, redirect, url_for, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from .tools import upload_file_to_s3

app = Flask(__name__)
app.config.from_envvar('APPSETTINGS')

class UploadForm(FlaskForm):
	file = FileField(label='File', validators=[
		FileRequired(),
		FileAllowed(['mp4'], message='Please convert to mp4')])

@app.route('/', methods=['GET', 'POST'])

def upload_page():
	form = UploadForm()
	if form.validate_on_submit():
		source = form.file.data
		filename = secure_filename(source.filename)
		output = upload_file_to_s3(source, app.config["S3_BUCKET"], filename)
		flash('{src} uploaded to S3 as {dst}'.format(src=filename, dst=output))
	return render_template('upload_form.html',
			title = 'Upload',
			form = form)

if __name__ == "__main__":
    app.run()