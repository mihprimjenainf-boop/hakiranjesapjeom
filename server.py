from flask import Flask, request
import os
app = Flask(__name__)



@app.route("/server_lozinka")
def rce():
    at = int(request.args.get("lozinka"))
    lozinka = os.environ.get("LOZINKA")
    if int(lozinka) == int(at):
        return "1"
    return "0"
