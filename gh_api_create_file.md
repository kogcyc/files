## api create file ##

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
file_name = 'aaa_' + base36.dumps(int(time.time())) + '.md'
repo.create_file(file_name, "commit message", bytes('texty text','utf-8'))
```
