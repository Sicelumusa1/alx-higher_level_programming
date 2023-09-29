#!/usr/bin/python3
"""
Defines a function that sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""


import requests
import sys


def get_x_request_id(url):
    """
    Sends an HTTP GET request to the URL and displays the value
    of the X-Request-Id in the header of the response, and display it.

    Args:
        url (str): The URL to send the request to
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id is not None:
            print(x_request_id)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":

    #  Get the URL from the command line argument
    url = sys.argv[1]

    #  Fetch and display the X-Request-Id from the URL response
    get_x_request_id(url)
