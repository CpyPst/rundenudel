#!/usr/bin/env python3

from flask import Flask, render_template, request
import os
import re

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
db = SQLAlchemy(app)

@app.route("/")
def home():
    return "<p>Home</p>"


@app.route("/offer/")
def offer_form():
    return render_template("offer.html")

@app.route("/offer-sent", methods=["POST"])
def process_offer():
    error = True
    if request.method == "POST":
        if "firstname" in request.form:
            error = False
        if "lastname" in request.form:
            error = False
        if "phone" in request.form:
            phone_regex = re.compile("(\(?([\d \-\)\–\+\/\(]+){6,}\)?([ .\-–\/]?)([\d]+))")
            if phone_regex.match(request.form["phone"]) is not None:
                error = False
        if "email" in request.form:
            error = False
        if "startdate" in request.form:
            error = False
        if "enddate" in request.form:
            error = False
        if "capacity" in request.form:
            error = False
        if "kidfriendly" in request.form:
            error = False
        if "petfriendly" in request.form:
            error = False
        if "street" in request.form:
            error = False
        if "zip" in request.form:
            error = False
        if "aptnumber" in request.form:
            error = False
        if "city" in request.form:
            error = False
        
        if error: 
            return "ERROR PAGE" # todo: render template with error message
        



