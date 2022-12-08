import requests
import json
from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.route("/Students")
def home():
    result= requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
    data_json=result.json()
    context={}
    context['title']="Students"
    context['students']=data_json['data']
    return render_template("mainPage.html",**context)

app.run(debug=True)
