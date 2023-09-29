#!/usr/bin/python3
"""
Defines a function that sends an HTTP GET request to the specified url,
retrieves the response body, and displays it.
"""

import requests
import sys


def fetch_url_content(url):
    """
    Sends an HTTP GET request to the specified url, retrieves the response
    body, and displays it. If the HTTP status code is than or equal to 400
    it print an error message

    Args:
        url (str): The URL to send the GET request to
    """
    try:
        response = requests.get(url)
        content = response.text

        if response.status_code >= 400:
            print("Error code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    #  Get the URL from the command line argument
    url = sys.argv[1]

    #  Fetch and display the URL content and handle HTTP errors
    fetch_url_content(url)
