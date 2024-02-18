def fetch_repos():
    auth_token = "Put Token here"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = "https://api.github.com/search/repositories"
    query = {
        "q": "machine learning in:description,readme,topics forks:>5 stars:>5 language:python is:public",
        "sort": "stars",
        "order": "desc",
        "per_page": "100"         
    }
    
    try:
        count = 1
        total_count = 0

        with open('project_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Count', 'Repo_Name', 'Description', 'Forks', 'Stars', 'Watchers', 'Open_Issues', 'Created_Date', 'Size']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            while total_count < 500:
                response = requests.get(url, params=query, headers=headers)
                response.raise_for_status()  # Raise an exception for HTTP errors
                data = response.json()
                for repo in data['items']:
                    writer.writerow({
                        'Count': count,
                        'Repo_Name': repo['name'],
                        'Description': repo['description'],
                        'Forks': repo['forks_count'],
                        'Stars': repo['stargazers_count'],
                        'Watchers': repo['watchers_count'],
                        'Open_Issues': repo['open_issues_count'],
                        'Created_Date': repo['created_at'], 
                        'Size': repo['size']
                    })

                    count += 1
                    total_count += 1

                if 'next' in response.links:
                    url = response.links['next']['url']
                else:
                    break

                
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
    except Exception as e:
        print(f"Error: {e}")

fetch_repos()
