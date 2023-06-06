
import os

import requests

username = "edyprasetyo"
access_token = "your_access_token"

clone_path = "/home/edy/Documents/MyProject/"
clone_url = f"https://{username}:{access_token}@github.com/{username}"

def get_github_repos(username):
    """Gets all the GitHub repositories for a given user."""
    url = "https://api.github.com/users/{}/repos".format(username)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Could not get GitHub repositories for user: {}".format(username))


repositories = get_github_repos(username)


for repo in repositories:
    print(repo["name"])
    repo_path = os.path.join(clone_path, repo["name"])
    clone_repo_url = f"{clone_url}/{repo['name']}.git"
    git_command = ""
    if os.path.isdir(repo_path):
        git_command = f"cd {repo_path} && git pull"
    else:
        git_command = f"git clone {clone_repo_url} {repo_path}"
    
    print(git_command)
    os.system(git_command)
