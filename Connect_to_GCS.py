import os 
from google.cloud import storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='dataproject-01-400611-570c885d198f.json'
storage_client=storage.Client()
bucket_name='data_project_bucket26MohamedMokhtar'
bucket=storage_client.bucket(bucket_name)
bucket=storage_client.create_bucket(bucket)

print(os.environ['PATHEXT'])
