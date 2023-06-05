
# S3 Boto3 Backup Automation

This Python script automates the backup process of a company's website files using Boto3. It allows the user to choose different actions to perform on an S3 bucket.

## Prerequisites

- Python 3
- Boto3 library (`pip install boto3`)
- AWS CLI configured with proper credentials

## Installation

Clone the repository:


git clone git@github.com:h93n/s3-boto3.git
cd your-repo


Install the required dependencies:


pip install -r requirements.txt


## Usage

1. Run the script:


python backup_script.py


2. Choose an action to perform by entering the corresponding number:

   1. Create a new S3 bucket
   2. Upload a single file
   3. Upload multiple files
   4. Download a file
   5. List all objects
   6. Delete the S3 bucket

3. Follow the prompts and provide the necessary information.

## References

- [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
