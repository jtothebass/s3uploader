# s3Uploader/helpers.py

import boto3, botocore
from flask import current_app as app

def upload_file_to_s3(file, bucket_name):
	s3 = boto3.client("s3",
		aws_access_key_id=app.config["S3_KEY"],
		aws_secret_access_key=app.config["S3_SECRET"]
		)

	try:
		s3.upload_fileobj(
			file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ContentType": file.content_type
            }
        )

	except Exception as e:
		# This is a catch all exception, edit this part to fit your needs.
		print("Something Happened: ", e)
		return e

	return "{}{}".format(app.config["URL"], file.filename)