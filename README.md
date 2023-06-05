# S3 Boto3 Backup Automation

This Python script automates the backup process of a company's website files using Boto3. It allows the user to choose different actions to perform on an S3 bucket.

## Prerequisites

- Python 3
- Boto3 library (`pip install boto3`)
- AWS CLI configured with proper credentials

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Install the required dependencies:
pip install -r requirements.txt

# Usage
Run the script:
python backup_script.py
Choose an action to perform by entering the corresponding number:
Create a new S3 bucket
Upload a single file
Upload multiple files
Download a file
List all objects
Delete the S3 bucket
Follow the prompts and provide the necessary information.

# References
Boto3 documentation
AWS CLI installation guide
