
import streamlit as st
import boto3

# Configurations
BUCKET_NAME = "my-bucket-name"

# Create a temporary folder to store uploaded files
if not os.path.isdir("tmp"):
    os.mkdir("tmp")

# Instantiate a client to interact with S3
s3_client = boto3.client('s3')

# Define function to upload files to S3
def upload_file(filename):
    s3_client.upload_file(filename, BUCKET_NAME, f"uploaded_files/{filename}")

# Define function to download files from S3
def download_file(filename):
    s3_client.download_file(BUCKET_NAME, f"{filename}", f"tmp/{filename}")


# Define function to retrieve list of files in S3 bucket
def list_files():
    file_list = []

    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)

    for obj in response['Contents']:
        file_list.append(obj['Key'])

    return file_list

def main():
    st.title("Data Visualization with Streamlit and AWS S3")

    # Upload file
    uploaded_file = st.file_uploader("Upload data file", type=["csv", "xlsx"])

    if uploaded_file:
        with open(f"tmp/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())

        upload_file(f"tmp/{uploaded_file.name}")
        st.success("File uploaded successfully")

    # List uploaded files
    st.header("Uploaded Files")
    file_list = list_files()
    for idx, file in enumerate(file_list):
        st.write(f"{idx+1}. {file}")

    # Download file
    file_to_download = st.selectbox("Select file to download", file_list)

    if file_to_download:
        download_file(file_to_download)
        st.success(f"File {file_to_download} downloaded successfully")

if __name__ == "__main__":
    main()
