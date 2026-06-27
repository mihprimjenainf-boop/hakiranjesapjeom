from flask import Flask, request
import os
app = Flask(__name__)

lozinka = os.environ.get("LOZINKA")

@app.route("/server_lozinka")
def rce():
    at = int(request.args.get("lozinka"))

    if int(lozinka) == int(at):
        return "1"
    return "0"
