""" flask hello test app """

import sys
import os

from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

"""
print(sys.version)
print("============================")
print(sys.version_info)
print("============================")
print(os.getcwd())
"""