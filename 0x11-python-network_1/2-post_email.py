#!/usr/bin/python3
"""
Defines a function that sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)

    Args:
        url (str): The URL to send the POST request to
        email (str): The email to send as a paramenter
    """
    try:
        #  Encode the email as a URL paramenter
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')

        #  Create a POST request
        req = urllib.request.Request(url, data, method='POST')

        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.URLError as e:
        print("Error:", e)

if __name__ == "__main__":
    #  Check if both URL and email arguments are provided
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    #  Get the URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    #  Send a POST request and display the response body
    send_post_request(url, email)
