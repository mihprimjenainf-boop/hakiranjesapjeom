#tvoje raćunalo
from flask import Flask, request
import os
import subprocess
app = Flask(__name__)
lozinka=123
@app.route("/server_lozinka")
def rce():
    at = int(request.args.get("lozinka"))
    print(type(at))
    if int(lozinka)==int(at):
        return '1'
    else:
        return '0'
app.run(host="127.0.0.1", port=8080)
