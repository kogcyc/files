from github import Github
import os

# Get GitHub token
shhhh = os.getenv('SHHHH')
if not shhhh:
    raise ValueError("Environment variable SHHHH not set!")

# Authenticate
g = Github(shhhh)

# Get authenticated user
user = g.get_user()
print(f"Authenticated as: {user.login}\n")

# Get all repositories
repos = user.get_repos()

# Function to recursively list files
def list_files(repo, path=""):
    contents = repo.get_contents(path)
    for content in contents:
        if content.type == "dir":
            list_files(repo, content.path)
        else:
            print(f"{repo.name} - {content.path}")

# Loop through repos
for repo in repos:
    try:
        list_files(repo)
    except Exception as e:
        print(f"Could not list files in {repo.name}: {e}")
