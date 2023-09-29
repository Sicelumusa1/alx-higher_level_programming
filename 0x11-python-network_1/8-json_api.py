#!/usr/bin/python3
"""
Defines a fucntion that sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter, and
display the response accordingly
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the
    letter as a parameter, and display the response accordingly

    Args:
        letter (str): The letter to send as the 'q' parameter
    """
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        if response.headers.get('content-type') == 'application/json':
            response_json = response.json()

            if response_json:
                user = response_json[0]
                print("[{}] {}".format(user.get('id'), user.get('name')))
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("No result")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    search_user(letter)
