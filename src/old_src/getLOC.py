import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
from urllib.parse import urlparse

df = pd.read_csv('dataset.csv')
df_cleaned = df.dropna(subset=['ML TD Type'])
filtered_df = df_cleaned[(df_cleaned['Comment-Removing Revision'] != "STILL_EXISTS") & (df_cleaned['ML TD Type'] != "nan")]

# Assuming you have a GitHub Personal Access Token for authentication
auth_token = "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"


headers = {
    "Authorization": f"token {auth_token}",
    "Accept": "application/vnd.github.v3+json"
}

for index, row in filtered_df.iterrows():
    sha = row['Comment-Removing Revision'].split('/')[-1]
    repo = row['Repo Name']
    filename = row['Filename']

    commit_url = f"https://api.github.com/repos/{repo}/commits/{sha}"
    response = requests.get(commit_url, headers=headers)
    commit_data = response.json()
    
    # Parse commit_data to find your file and its patch_url
    for file in commit_data.get("files", []):
        if file["filename"] == filename:
            changesInFile = file["changes"]
            filtered_df.loc[index, 'Changes LOC'] = changesInFile;
            break
    # Get size of the project
    repos_url = f"https://api.github.com/repos/{repo}"
    response = requests.get(repos_url, headers=headers)
    repos_data = response.json()
    if response.status_code == 200:
        size = repos_data["size"]
        filtered_df.loc[index, 'Project size in KB'] = size;

filtered_df.to_csv('filtered_data_with_loc2.csv', index=False)