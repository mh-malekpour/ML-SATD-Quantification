import requests

def fetch_ml_repositories():
    auth_token = "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"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = "https://api.github.com/search/repositories"
    query = {"q": "machine learning in:description,readme,topics forks:>5 stars:>5 language:python",
        "sort": "stars",
        "order": "desc",
        "per_page": "100"         
    }
    
    try:
        response = requests.get(url, params=query, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        count = 1

        for repo in data['items']:
            print(f"Count: {count}")
            print(f"Repo Name: {repo['name']}")
            print(f"Description: {repo['description']}\n")
            count += 1
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
    except Exception as e:
        print(f"Error: {e}")

fetch_ml_repositories()