
import os

import requests

username = "edyprasetyo"
access_token = "your"

clone_path = "/home/edy/Documents/MyProject/"
clone_url = f"https://{username}:{access_token}@github.com/{username}"

def cloneRepo(repositories):
    print(repositories)
    for repo in repositories:     
        repo_path = os.path.join(clone_path, repo["name"])
        clone_repo_url = f"{clone_url}/{repo['name']}.git"
        git_command = ""
        if os.path.isdir(repo_path):
            git_command = f"cd {repo_path} && git pull"
        else:
            git_command = f"git clone {clone_repo_url} {repo_path}"
        
        print(git_command)
        os.system(git_command)



headers = {
    'Authorization': f'token {access_token}'
}

# Get public repositories
public_repo_url = f'https://api.github.com/users/{username}/repos'
response = requests.get(public_repo_url, headers=headers)
public_repos = response.json()

# Get private repositories
private_repo_url = f'https://api.github.com/user/repos'
response = requests.get(private_repo_url, headers=headers)
private_repos = response.json()

cloneRepo(public_repos)
cloneRepo(private_repos)


