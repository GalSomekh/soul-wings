# soul-wings

Web server that enables uploading video and audio testimonials, automatic transcription and textual search over their content.

----

## Installation and Packages
1. Clone the benchmarker repo to your local machine  
2. Install the required packages: `pip install -r requirements.txt`
3. Install `ffmpeg`. In Mac: `brew install ffmpeg`

## Secrets Setup
1. In your copy of the repo, create a folder called `proj_secrets`
2. Login to Soulwings AWS > S3 > `soul-wings-secrets` and download both files to the `proj_secrets` folder you created
3. Copy the full path of the file named `soulwings-....json`
4. Create an ENV variable named `GOOGLE_APPLICATION_CREDENTIALS` with the value of the path you copied. In Mac:
```bash
vim ~/.bash_profile
# Add this line to the file: #
export GOOGLE_APPLICATION_CREDENTIALS='<copied path>'
```

----

## Running Locally
Simply execute `python application.py`.
Make sure you're using Python3, `python3 application.py` can do the trick.

----

## Deploying and DevOps
1. The web server is managed by AWS Elastic Beanstalk. This AWS service manages deployment of new versions, EC2 and other related AWS services. The folder `.ebextensions` has settings for AWS Elastic Beanstalk.
2. AWS CodePipeline starts the deployment process after each merge to the master repo with a webhook.
3. Mongo is hosted in Mongo Atlas and transcription is done in Google Cloud.
