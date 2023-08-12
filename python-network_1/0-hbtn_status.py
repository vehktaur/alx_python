"""
task 0 module
"""
import requests


req = requests.get("https://alu-intranet.hbtn.io/status")

print("Body response:")
print("\t- type:", type(req.text))
print("\t- content:", req.text)