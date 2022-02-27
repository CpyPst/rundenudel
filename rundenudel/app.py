#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, Response
import os
import re
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, DateField, BooleanField
from wtforms.validators import Length, DataRequired, Regexp, NumberRange, Email
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.secret_key = os.getenv("FLASK_KEY")
db = SQLAlchemy(app)

# Database Class for Accomodation
class Accomodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostid = db.Column(db.Integer, db.ForeignKey("host.id"))
    startdate = db.Column(db.Date, nullable=False)
    enddate = db.Column(db.Date, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    kidfriendly = db.Column(db.Boolean, default=False)
    petfriendly = db.Column(db.Boolean, default=False)
    street = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    aptnumber = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String, nullable=False)
    additional = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Accomodation %r>" % self.id


# Database Class for Host
class Host(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String, nullable=True)
    accomodations = db.relationship("Host", backref="accomodation", primaryjoin="host.id == accomodation.id")

    def __repr__(self):
        return "<Host %r>" % self.id


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
        return render_template("/confirmation.html")
        #return redirect("/confirmation")
    else:
        return render_template("offer.html", form=form)



def handle_offer(form):
    try:
        host_id = create_host(form.firstname, form.lastname, form.email, form.phone)
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

