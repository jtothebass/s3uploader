# s3Uploader/config.py

import os

S3_BUCKET                 = "Target Bucket"
S3_KEY					  = "S3 Key Here"
S3_SECRET				  = "S3 Secret Here"
URL						  = "Cloudfront URL here"

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000