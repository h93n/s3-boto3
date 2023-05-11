import logging
import boto3
from botocore.exceptions import ClientError
import os




def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def create_bucket(s3_client,bucket_name,region):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(s3,file_name, bucket, object_name=None):
    

    s3.download_file(bucket, file_name, file_name)
   
def listBuckets(s3):
    # Retrieve the list of existing buckets

    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
    	print(f'  {bucket["Name"]}')
    	
    	
    	
    	
def listfiles(s3,bucket_name):
    # Retrieve the list of existing buckets

    response = s3.list_buckets()

    response = s3.list_objects(Bucket=bucket_name)

    if 'Contents' in response:
    	for item in response['Contents']:
        	print(item['Key'])
    else:
    	print('Bucket is empty')
    	
    	
def uploadMulti_file(s3, bucket):
   
# Prompt user to select files to upload
    print("Select the files to upload:")
    file_names = []
    while True:
    	file_name = input("> ")
    	if file_name == "":
        	break
    	file_names.append(file_name)
# Upload files to S3 bucket
    for i, file_name in enumerate(file_names):
        object_name = file_names[i]
        s3.upload_file(file_name, bucket, object_name)
        print(f"{file_name} uploaded as {file_name} to S3 bucket {bucket}")


    
   

def deleteBucketNotEmpty(s3, bucket):
    # Set the name of the bucket you want to delete
    

# Delete all objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket)
    if 'Contents' in response:
       for obj in response['Contents']:
           s3.delete_object(Bucket=bucket, Key=obj['Key'])
# Delete the bucket itself
    s3.delete_bucket(Bucket=bucket)
    
    
    
    
    
	
def main_menu():
    """Display the main menu and execute the user's choice"""
    region="us-west-2"
    s3 = boto3.client('s3')
    print("Select an option:")
    print("1. Create a bucket")
    print("2. Upload a file to a bucket")
    print("3. Upload multiple files to a bucket")
    print("4. download  a file from a bucket")
    print("5. delete bucket ")
    print("6. Exit")

    choice = input("Enter option number: ")
    if choice == "1":
        listBuckets(s3)
        bucket_name = input("Enter bucket name: ")
        created = create_bucket(s3,bucket_name,region)
    
    elif choice == "2":
        listBuckets(s3)
        bucket = input("Enter bucket name: ")
        listfiles(s3,bucket)
        file_name = input("Enter file name: ")
        upload_file(file_name, bucket, file_name)
    elif choice == "3":
        listBuckets(s3)
        bucket = input("Enter bucket name: ")
        listfiles(s3,bucket)
        #file_name = input("Enter file name from the list: ")
        uploadMulti_file(s3, bucket)
    elif choice == "4":
        listBuckets(s3)
        bucket = input("Enter bucket name: ")
        listfiles(s3,bucket)
        file_name = input("Enter file name from the list: ")
        download_file(s3,file_name, bucket, file_name)
    elif choice == "5":
        listBuckets(s3)
        bucket = input("Enter bucket name to delete: ")
        deleteBucketNotEmpty(s3, bucket)
        
    elif choice == "6":
        print("Exiting program...")
        return
    else:
        print("Invalid option. Please try again.")
    
    main_menu()  # display the menu again after executing the chosen function

if __name__ == "__main__":
    main_menu()
