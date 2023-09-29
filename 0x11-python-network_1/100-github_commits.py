#!/usr/bin/python3
"""
Defines a function that fetches the 10 most recent commits from a
github repository by the given user
"""

import requests
import sys


def fetch_recent_commits(repo_name, owner_name):
    """
    Fetches the 10 most recent commits from agithub repository by
    the given user

    Args:
        repo_name (str): The name of the github repository
        owner_name (str): The username of the repository owner
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()

        commits = response.json()

        if commits:
            for commit in commits[:10]:
                sha = commit.get('sha')
                author = commit.get('commit').get('author').get('name')
                print(f"{sha}: {author}")
        else:
            print("No commits found")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_recent_commits(repo_name, owner_name)
