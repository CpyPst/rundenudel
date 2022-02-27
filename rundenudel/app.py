#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, Response
import os
import re
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, DateField, BooleanField
from wtforms.validators import Length, DataRequired, Regexp, NumberRange, Email
from flask_sqlalchemy import SQLAlchemy
from rundenudel import Host, Accomodation

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.secret_key = os.getenv("FLASK_KEY")
db = SQLAlchemy(app)


def checked(form, field):
    if not field.data:
        raise ValidationError("Checkbox must be checked.")


class OfferForm(FlaskForm):
    firstname = StringField("firstname", [Length(max=45), DataRequired()])
    lastname = StringField("lastname", [Length(max=45), DataRequired()])
    phone = StringField(
        "phone",
        [DataRequired(), Regexp("(\(?([\d \-\)\–\+\/\(]+){6,}\)?([ .\-–\/]?)([\d]+))")],
    )
    email = EmailField("email", [DataRequired(), Email()])
    startdate = DateField("startdate", [DataRequired()], format="%Y-%m-%d")
    enddate = DateField("enddate", [DataRequired()], format="%Y-%m-%d")
    capacity = IntegerField("capacity", [DataRequired(), NumberRange(min=1, max=1000)])
    kidfriendly = BooleanField("kidfriendly")
    petfriendly = BooleanField("petfriendly")
    street = StringField("street", [DataRequired(), Length(max=45)])
    zipcode = StringField(
        "zipcode", [DataRequired(), Regexp(r"^[0-9]{5}"), Length(max=5)]
    )
    aptnumber = StringField(
        "aptnumber", [DataRequired(), Regexp(r"^[0-9]{1,3}[a-zA-Z]?\b")]
    )
    city = StringField("city", [DataRequired(), Length(max=45)])
    dsgvo = BooleanField("dsgvo", [DataRequired(), checked])


@app.route("/")
def home():
    return redirect("/offer")


@app.route("/offer/", methods=["GET", "POST"])
def offer_form():
    form = OfferForm()
    if form.validate_on_submit():
        handle_offer(form)
        return redirect("/confirmation/")
    else:
        return render_template("offer.html", form=form)


def handle_offer(form):
    accomodation = Accomodation(
        hostid=host_id,
        startdate=form.startdate,
        enddate=form.enddate,
        capacity=form.capacity,
        kidfriendly=form.kidfriendly,
        petfriendly=form.petfriendly,
        street=form.street,
        zipcode=form.zipcode,
        aptnumber=form.aptnumber,
        city=form.city,
        additional=form.additional,
    )
    try:
        host_id = create_host(form.firstname, form.lastname, form.email, form.phone)
        db.session.add(accomodation)
        db.session.commit()
    except Exception as e:
        print(e)


def create_host(firstname, lastname, email, phone):
    exists = Host.query.filter_by(
        firstname=firstname, lastname=lastname, email=email
    ).first()
    if exists:
        return exists.id
    host = Host(firstname=firstname, lastname=lastname, email=email, phone=phone)
    db.session.add(host)
    db.session.commit()
    db.session.refresh(host)
    return host.id

