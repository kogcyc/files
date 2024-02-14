#!/usr/bin/python3

from github import Github
import os
from sys import argv, exit

file_name = argv[1]
repo_name = argv[2]

force_overwrite = False
if len(argv) > 3:
    if argv[3] == 'true':
        force_overwrite = True
    else:
        force_overwrite = False

with open(file_name, 'rb') as f:
    file_contents = f.read()  

shhhh = os.getenv('some_secret')
if shhhh is None:
    print("Error: GitHub token not found in environment variable some_secret")
    exit(1)

github_api = Github(shhhh)
repo_name = 'kogcyc/' + repo_name # you might want to change this to your user id
repo = github_api.get_repo(repo_name)

try:
    contents = repo.get_contents(file_name)
    print("\033[91m" + "That file exists" + "\033[0m")
    
    if force_overwrite:
        repo.delete_file(contents.path, "Remove existing file", contents.sha)
        print("\033[96m" + "Forced overwrite requested" + "\033[0m")
        repo.create_file(file_name, "New file", file_contents, branch="main")
        print("\033[93m" + "File overwritten successfully" + "\033[0m")
except:
    print("\033[92m" + "That file does not exist" + "\033[0m")
    repo.create_file(file_name, "New file", file_contents, branch="main")
    print("\033[92m" + "File created successfully" + "\033[0m")
