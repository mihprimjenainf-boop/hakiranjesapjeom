from flask import Flask, request

app = Flask(__name__)

lozinka = 123

@app.route("/server_lozinka")
def rce():
    at = int(request.args.get("lozinka"))

    if lozinka == at:
        return "1"
    return "0"
