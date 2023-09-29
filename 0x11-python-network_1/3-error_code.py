#!/usr/bin/python3
"""
Defines a function that sends a request to the URL and displays the
body of the response (decoded in utf-8). Handles urllib.error.HTTPError
exceptions
"""

import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    """
    Sends a request to the URL and displays the body of the response 
    (decoded in utf-8). Handles urllib.error.HTTPError exceptions

    Args:
        url (str): The URL to send the GET request to
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = request.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)

if __name__ == "__main__":
    #  Check if a URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    #  Get the uRl from the command line argument
    url = sys.argv[1]

    #  Fetch and display the URL content or handle HTTP error
    fetch_url_content(url)
