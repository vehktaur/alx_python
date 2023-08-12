"""
module documentation
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]


# Send a GET request to the GitHub API for user information
response = requests.get("https://api.github.com/user", auth= (username, password))

# Check if the request was successful
user_info = response.json()
user_id = user_info.get("id")
print(user_id)

