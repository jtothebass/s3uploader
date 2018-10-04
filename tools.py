# s3uploader/tools.py

import os
import boto3, botocore
from flask import current_app as app

#class ProgressPercentage(object):
#	def __init__(self, filename):
#		self._filename = filename
#		self._size = float(os.path.getsize(filename))
#		self._seen_so_far = 0
#		self._lock = threading.Lock()
#
#	def __call__(self, bytes_amount):
#		with self._lock:
#			self._seen_so_far += bytes_amount
#			percentage = (self._seen_so_far / self._size) * 100
#			sys.stdout.write(
#				"\r%s  %s / %s  (%.2f%%)" % (
#					self._filename, self._seen_so_far, self._size, percentage))
#			sys.stdout.flush()

def upload_file_to_s3(file, bucket_name, filename):
	dest_file = filename
	tempdir = '/tmp/'
	tempfile = tempdir + dest_file
	#Set up S3 boto client
	client = boto3.client("s3", 'us-east-1', aws_access_key_id=app.config["S3_KEY"], aws_secret_access_key=app.config["S3_SECRET"])
	# Upload
	try:
		client.upload_fileobj(
			file,
            bucket_name,
            filename,
            ExtraArgs={
                "ContentType": file.content_type
            })

	except Exception as e:
		# This is a catch all exception, edit this part to fit your needs.
		print("Something Happened: ", e)
		return e

	return "{}{}".format(app.config["URL"], dest_file)