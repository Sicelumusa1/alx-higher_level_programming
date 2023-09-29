#!/usr/bin/python3
"""
Defines a function that fetches https://alx-intranet.hbtn.io/status
"""

import requests


def fetch_url_content(url):
    """
    Fetches the content od a URL using the request package and displays it

    Args:
        url (str): The URL to fetch content from.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        content = response.text

        print("Body response:")
        print("\t- type: {}", type(content))
        print("\t- content:", content)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    #  Define the URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    #  Fetch and display the URL content
    fetch_url_content(url)
