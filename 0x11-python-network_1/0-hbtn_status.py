#!/usr/bin/python3
"""
Defines a fuction that fetches the content of a URL and displays it in a
specific format
"""

import urllib.request


def fetch_url_content(url):
    """
    Fetches the content of a URL and displays it in a specific format

    Args:
        url (str): The URL to fetch content from
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            content_str = content.decode('utf-8')

            print("Body responce:")
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", content_str)
    except urllib.error.URLError as e:
        print("Error:", e)

if __name__ == "__main__":
    #  Define the URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    #  Fetch and display the URL content
    fetch_url_content(url)
