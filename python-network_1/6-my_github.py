"""
module documentation
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

session = requests.Session()
session.auth = (username, password)


# Send a GET request to the GitHub API for user information
response = session.get("https://api.github.com/user")

# Check if the request was successful
user_info = response.json()
user_id = user_info.get("id")
print(user_id)

