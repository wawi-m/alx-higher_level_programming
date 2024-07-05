#!/usr/bin/python3
import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter,
    and displays the body of the response.

    Args:
    - url (str): The URL to send the POST request to.
    - email (str): The email address to send as a parameter.

    Prints:
    - The body of the response from the POST request.
    """
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        print("Body response:")
        print("\t- {}".format(response.text))
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
