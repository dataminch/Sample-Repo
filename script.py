import sys

# import os
# import math
import requests

# use sys.executable for python path
# create virtual environment
# python -m venv venv
# pip install requests
print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://berkeleykaraoke.net")
print(r.status_code)
