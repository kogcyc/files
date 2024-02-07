## api delete files ##

```python
from github import Github
from github import Auth
import os
import base36
import time
shhhh = os.getenv('SHHHH')
auth = Auth.Token(shhhh)
gitub_api = Github(auth=auth)
repo_name = "<userID>/<repoNAME>"
repo = gitub_api.get_repo(repo_name)
contents = repo.get_contents("")
or file in contents:
    print(file.path)
    repo.delete_file(file.path, "removed", file.sha)
