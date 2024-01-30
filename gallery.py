
from github import Github
from github import Auth

auth = Auth.Token("")
g = Github(auth=auth)
repo_name = "kogcyc/files"
file_path = "aaa.html"
repo = g.get_repo(repo_name)
try:
    contents = repo.get_contents(file_path)
    repo.delete_file(file_path, "commit message", contents.sha)
    print(f"File '{file_path}' deleted successfully.")
except Exception as e:
    print(f"Failed to delete file '{file_path}': {e}")


b = """
"""

b = b + "hello,\n" + "<br>there!"

a = """
<!doctype html>
<html lang="en">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
      html {
        background: #68a;
        color: #fff;
        font-family: sans-serif;
        font-size: 1em;
      }
    </style>

    <body>

"""

c = """
    </body>

</html>

"""

d = a + b + c

repo.create_file(file_path, "commit message", d)
