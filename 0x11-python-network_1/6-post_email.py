#!/usr/bin/python3
"""
Defines a function that sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""

import requests
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    retrieves and displays the body of the response

    Args:
        url (str): The URL to send the POST request to
        email (str): The email to send as a paramenter
    """
    try:
        data = {'email': email}
        response = requests.post(url, data=data)
        response.raise_for_status()

        content = response.text
        print(content)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":

    #  Get the URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    #  Send a POST request and display the response body
    send_post_request(url, email)
