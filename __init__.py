# s3Uploader/__init__.py

from flask import Flask, render_template, request, redirect
from flask_wtf import Form
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
from .helpers import upload_file_to_s3

app     = Flask(__name__)
app.config.from_envvar('APPSETTINGS')

class UploadForm(Form):
    file = FileField('Choose File')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        output = upload_file_to_s3(form.file, app.config["S3_BUCKET"])
        flash('{src} uploaded to S3 as {dst}'.format(src=form.file.data.filename, dst=output))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()