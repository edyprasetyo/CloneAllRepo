import os

import requests

username = 'your_username'
api_token = 'your_api_token'

clone_folder = "/home/edy/Documents/GitProject/"

url = f"https://gitlab.com/api/v4/projects?per_page=1000&visibility=private"

headers = {
    'Private-Token': f'{api_token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    repositories = response.json()    

    for repo in repositories:
        repoUrl = "https://oauth2:"+ api_token +"@gitlab.com/"+ username +"/" + repo["name"] + ".git"
        print(repoUrl)
        if os.path.isdir(clone_folder + repo["name"]):
            print("git pull")
            os.system("cd " + clone_folder + repo["name"] + " && git pull")
        else:
            print("git clone")
            os.system("git clone " + repoUrl + " " + clone_folder + repo["name"])
else:
    print(f"Failed to retrieve repositories. Status code: {response.status_code}")
