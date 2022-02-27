from flask_sqlalchemy import SQLAlchemy
from rundenudel import db


class Accomodation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincre=True, nullable=False)
    hostid = db.Column(db.Integer, db.ForeignKey("user.id"))
    startdate = db.Column(db.Date, nullable=False)
    enddate = db.Column(db.Date, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    kidfriendly = db.Column(db.Boolean, default=False)
    petfriendly = db.Column(db.Boolean, default=False)
    street = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.Char(5), nullable=False)
    aptnumber = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String, nullable=False)
    additional = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Accomodation %r>" % self.id


class Host(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincre=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String, nullable=True)
    accomodations = db.relationship("Host", backref="accomodation")

    def __repr__(self):
        return "<Host %r>" % self.id
