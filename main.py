from flask import Flask, render_template, json
#from test import *
import requests
import threading
import time
from flask_csv import send_csv
import os
import tablib


app = Flask(__name__)

@app.route("/")
def home():
    # static/data/test_data.json
    #filename = os.path.join(app.static_folder, 'data', 'screen13.json')
    #screen1 = []
    screen2 =[]
    screen3 =[]
    screen4 =[]
    screen5 =[]
    screen6 =[]
    screen7 =[]
    screen8 =[]
    screen9 =[]
    screen10 =[]
    screen11 =[]
    screen12 =[]
    screen13 =[]
    screen14 =[]
    with open('static/data/Sal 2.json', 'r') as f:
        screen2 = json.load(f)
        f.close()
    with open('static/data/Sal 3.json', 'r') as f:
        screen3 = json.load(f)
        f.close()
    with open('static/data/Sal 4.json', 'r') as f:
        screen4 = json.load(f)
        f.close()
    with open('static/data/Sal 5.json', 'r') as f:
        screen5 = json.load(f)
        f.close()
    with open('static/data/Sal 6.json', 'r') as f:
        screen6 = json.load(f)
        f.close()
    with open('static/data/Sal 7.json', 'r') as f:
        screen7 = json.load(f)
        f.close()
    with open('static/data/Sal 8.json', 'r') as f:
        screen8 = json.load(f)
        f.close()
    with open('static/data/Sal 9.json', 'r') as f:
        screen9 = json.load(f)
        f.close()
    with open('static/data/Sal 10.json', 'r') as f:
        screen10 = json.load(f)
        f.close()
    with open('static/data/Sal 11.json', 'r') as f:
        screen11 = json.load(f)
        f.close()
    with open('static/data/Sal 12.json', 'r') as f:
        screen12 = json.load(f)
        f.close()
    with open('static/data/Sal 13.json', 'r') as f:
        screen13 = json.load(f)
        f.close()
    with open('static/data/Sal 14.json', 'r') as f:
        screen14 = json.load(f)
        f.close()

    return render_template("home.html", data2=screen2, data3=screen3, data4=screen4, data5=screen5,
                                        data6=screen6, data7=screen7, data8=screen8, data9=screen9,
                                        data10=screen10, data11=screen11, data12=screen12, data13=screen13,
                                        data14=screen14)#data=data

@app.route("/settings")
def settings():

    return render_template("settings.html")

@app.route("/about")
def about():

    return render_template("about.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)