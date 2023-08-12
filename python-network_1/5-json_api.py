"""
module documentation
"""

import requests
import sys

q = "No result"

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if type(arg) is str:
        q = arg
        
        payload = {"q" : q}
        
        r = requests.post("http://0.0.0.0:5000/search_user", data = payload)
        
        try:
            text = r.json()
            
            if text:
                id = text.get("id")
                name = text.get("name")
                print("[{}] {}".format(id, name))
            else:
                print("No result")
        except:
            print("Not a valid JSON") 

