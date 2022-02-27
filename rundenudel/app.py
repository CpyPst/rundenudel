#!/usr/bin/env python3

import email
from flask import Flask, render_template, request
import os
import re
from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    EmailField,
    IntegerField,
    DateField,
    BooleanField,
)
from wtforms.validators import Length, DataRequired, regexp, NumberRange, Email
from rundenudel import Accomodation, Host

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.secret_key = os.getenv("FLASK_KEY")
db = SQLAlchemy(app)


class OfferForm(FlaskForm):
    firstname = StringField("firstname", [Length(max=45), DataRequired()])
    lastname = StringField("lastname", [Length(max=45), DataRequired()])
    phone = StringField(
        "phone",
        [DataRequired(), regexp("(\(?([\d \-\)\–\+\/\(]+){6,}\)?([ .\-–\/]?)([\d]+))")],
    )
    email = EmailField("email", [DataRequired(), Email()])
    startdate = DateField("startdate", [DataRequired()], format="%d.%M.%Y")
    enddate = DateField("startdate", [DataRequired()], format="%d.%M.%Y")
    capacity = IntegerField("capacity", [DataRequired(), NumberRange(min=1, max=1000)])
    kidfriendly = BooleanField("kidfriendly")
    petfriendly = BooleanField("petfriendly")
    street = StringField("street", [DataRequired(), Length(max=45)])
    zipcode = StringField("zipcode", [DataRequired(), regexp("^[0-9]{5}\b")])
    aptnumber = StringField(
        "aptnumber", [DataRequired(), regexp("^[0-9]{1,3}[a-zA-Z]?\b")]
    )
    city = StringField("city", [DataRequired(), Length(max=45)])
    dsgvo = BooleanField("dsgvo", [DataRequired(), checked])

@app.route("/")
def home():
    return redirect("/offer")

@app.route("/offer/", methods=["GET", "POST"])
def offer_form():
    return render_template("offer.html")


@app.route("/submit-offer", methods=["POST"])
def process_offer():
    form = OfferForm()
    if form.validate_on_submit():
        # DB OPERATION
        return redirect("/confirmation")


def handle_offer(form):
    try:
         create_host(form.firstname, form.lastname, form.email, form.phone)
    
    db.session.add()


def create_host(firstname, lastname, email, phone):
    if Host.query.filter_by(
        firstname=firstname, lastname=lastname, email=email
    ).first():
        raise AlreadyExistsException("")
    host = Host(firstname=firstname, lastname=lastname, email=email, phone=phone)
    db.session.add(host)
    db.session.commit()
