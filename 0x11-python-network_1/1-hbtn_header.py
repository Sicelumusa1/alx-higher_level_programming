#!/usr/bin/python3
"""
Defines a function that sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""


import urllib.request
import sys


def get_x_request_id(url):
    """
    Sends a request to the URL and displays the value of the X-Request-Id
    variable found in the header of the response, and display it.

    Args:
        url (str): The URL to send the request to
    """
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id is not None:
                print(x_request_id)
    except urllib.error.URLError as e:
        print("Error:", e)


if __name__ == "__main__":
    #  Check if a URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    #  Get the URL from the command line argument
    url = sys.argv[1]

    #  Fetch and display the X-Request-Id from the URL response
    get_x_request_id(url)
