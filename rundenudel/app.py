#!/usr/bin/env python3

from flask import Flask, render_template, request
import os
import re
from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, IntegerField, DateField, BooleanField
from wtforms.validators import Length, DataRequired, regexp, NumberRange, Email

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
db = SQLAlchemy(app)

class OfferForm(FlaskForm):
    firstname = StringField("firstname", [Length(max=45), DataRequired()])
    lastname = StringField("lastname", [Length(max=45), DataRequired()])
    phone = StringField("phone", [DataRequired(), regexp("(\(?([\d \-\)\–\+\/\(]+){6,}\)?([ .\-–\/]?)([\d]+))")])
    email = EmailField("email", [DataRequired(), Email()])
    startdate = DateField("startdate", [DataRequired()], format='%d.%M.%Y')
    enddate = DateField("startdate", [DataRequired()], format='%d.%M.%Y')
    capacity = IntegerField("capacity", [DataRequired(), NumberRange(min=1, max=1000)]) 
    kidfriendly = BooleanField("kidfriendly") 
    petfriendly = BooleanField("petfriendly")
    street = StringField("street", [DataRequired(), Length(max=45)])
    zipcode = StringField("zipcode", [DataRequired(), regexp("^[0-9]{5}\b")])
    aptnumber = StringField("aptnumber", [DataRequired(), regexp("^[0-9]{1,3}[a-zA-Z]?\b")])
    city = StringField("city", [DataRequired(), Length(max=45)])



@app.route("/")
def home():
    return "<p>Home</p>"


@app.route("/offer/")
def offer_form():
    return render_template("offer.html")

@app.route("/submit-offer", methods=["POST"])
def process_offer():
    form = OfferForm()
    if form.validate_on_submit():
        # DB OPERATION
        return redirect("/confirmation")
        



