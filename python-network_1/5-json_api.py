"""
module documentation
"""

import requests
import sys

q = ""

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if type(arg) is str:
        q = arg
        
        payload = {"q" : q}
        
        r = requests.post("http://0.0.0.0:5000/search_user", data = payload)
        
        text = r.json()
        
        if text:
            id = text.get("id")
            name = text.get("name")
            if id is not None and name is not None:
                print("[{}] {}".format(id, name))
            else:
                print("Not a valid JSON")
        else:
            print("No result") 
        
