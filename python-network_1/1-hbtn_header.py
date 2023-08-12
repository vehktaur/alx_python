"""
module documentation
"""

import requests
import sys

url = sys.argv[1]

req = requests.get(url)

content = req.headers.get("X-Request-Id")

print(content)
