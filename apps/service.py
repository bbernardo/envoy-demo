from flask import Flask
from flask import request
import socket
import os
import sys
import requests

app = Flask(__name__)

@app.route('/service/<service_id>')
def service(service_id):
    if (os.environ['SERVICE_NAME']) == 'a':
        ret = requests.get("http://localhost:9000/trace/b")

    return ('Hello from {} (hostname: {} resolvedhostname:{})\n'.format(
                    os.environ['SERVICE_NAME'],
                    socket.gethostname(),
                    socket.gethostbyname(socket.gethostname())))

@app.route('/trace/<service_id>')
def trace(service_id):
    if (os.environ['SERVICE_NAME']) == 'a':
        ret = requests.get("http://localhost:9000/trace/b")

    return service(service_id)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

