from github import Github
import os

# Get the GitHub token from environment variable
shhhh = os.getenv('SHHHH')
if not shhhh:
    raise ValueError("Environment variable SHHHH not set!")

# Authenticate
g = Github(shhhh)

# Define the repo name
repo_name = "kogcyc/files"

# Get the repository
repo = g.get_repo(repo_name)

# Get the contents of the root directory
contents = repo.get_contents("")

# Loop through the files and print their paths
for file_content in contents:
    print(file_content.path)

