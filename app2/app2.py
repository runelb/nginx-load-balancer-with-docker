from flask import Flask
import os
import socket

app = Flask(__name__)
@app.route("/")

def hello():
    server_name = "Server 2"
    html = "<h3>Hello, this is {name}!</h3> <b>Hostname:</b> {hostname}<br/>"
    return html.format(name=server_name, hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)