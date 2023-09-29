#!/usr/bin/python3
"""
Defines a function that uses basic Authentication with a GitHub personal
access token to access user information and display the user ID
"""

import requests
import sys


def get_user_id(username, access_token):
    """
    Uses Basic Authentication with a GitHub personalaccess token to
    access user information and display the user ID

    Args:
        username (str): your github username
        access_token (str):your github personal access token
    """
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, access_token))
        response.raise_for_status()

        if response.status_code == 200:
            user_info = response.json()
            user_id = user_info.get('id')
            print(user_id)
        else:
            print("None")
    except requests.exceptions.RequestException:
        print("None")


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]

    get_user_id(username, access_token)
