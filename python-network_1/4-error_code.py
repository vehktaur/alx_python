"""
module documentation
"""

import requests
import sys

url = sys.argv[1]

r = requests.get(url)

status = r.status_code
if status >= 400:
    print("Error code : {}".format(status))