"""
module documentation
"""

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]
payload = {"email": email}

r = requests.post(url, data=payload)

request_email = r.text

print(request_email)