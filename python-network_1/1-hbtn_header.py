"""
module documentation
"""

import requests 
import sys

url = sys.argv[1]

req = requests.get(url)

content = req.headers["X-Request-Id"]

if len(content) > 0:
    print(req.headers["X-Request-Id"])
else:
    print(None)


