"""
module documentation
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

session = requests.Session()
session.auth = (username, password)

try:
    # Send a GET request to the GitHub API for user information
    response = session.get("https://api.github.com/user")
    
    # Check if the request was successful
    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info["id"]
        print(f"{user_id}")
    else:
        print(f"None")
    
except requests.RequestException as e:
    print("An error occurred:", e)
    sys.exit(1)