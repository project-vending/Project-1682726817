
import os

project_name = "data_visualization_with_streamlit_and_aws_s3"

folders = ["data", "src", "tests"]
files = ["README.md", "app.py"]

for folder in folders:
    os.makedirs(os.path.join(project_name, folder))

for file in files:
    open(os.path.join(project_name, file), 'a').close()
    
print("Project file structure created successfully!")
