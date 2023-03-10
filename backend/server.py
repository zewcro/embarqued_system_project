import subprocess
from os import name
from flask import Flask,redirect,render_template
from flask_cors import CORS


import urllib.request as urllib2

        
app = Flask("webserver_embeded")
CORS(app)


@app.route('/', methods=["GET"])
def say_hello():
    return render_template('../frontend/templates/index.html')


@app.route('/captor_data', methods=["GET"])
def captor_data():
    response = urllib2.urlopen("http://10.8.128.135/")
    data = response.read()
    return data


def send_mqtt_captor_data():
    subprocess.call(["python", "main.py"])
    return "data sended :) "


def extract_data_from_html():
    pass


if __name__ == '__main__':
    app.run(port=5000)  