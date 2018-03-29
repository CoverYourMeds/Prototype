import os

from flask import render_template, Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Get app config from absolute file path
if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

# Create DB after config
db = SQLAlchemy(app)

# Import Model after DB set
from CoverYourMeds.models import Medication, Times


@app.route("/", methods=["GET"])
def home():
    db.create_all()

    times = Times.query.all()
    schedule = make_schedule(times)
    return render_template("index.html", schedule=schedule)


@app.route("/mymeds", methods=["GET"])
def mymeds():
    db.create_all()

    # Grab all medications from database
    medications = Medication.query.all()
    return render_template("mymeds.html", medications=medications)


@app.route("/settings", methods=["GET"])
def settings():
    return render_template("settings.html")


def make_schedule(times):
    schedule = {"sun": {}, "mon": {}, "tues": {}, "wed": {}, "thur": {}, "fri": {}, "sat": {}}
    for time in times:
        if time.sun:
            if time.time in schedule["sun"]:
                schedule["sun"][time.time].append(Medication.query.filter_by(med_id=time.medication).first())
            else:
                schedule["sun"][time.time] = [Medication.query.filter_by(med_id=time.medication).first()]
        if time.mon:
            if time.time in schedule["mon"]:
                schedule["mon"][time.time].append(Medication.query.filter_by(med_id=time.medication).first())
            else:
                schedule["mon"][time.time] = [Medication.query.filter_by(med_id=time.medication).first()]
        if time.tues:
            if time.time in schedule["tues"]:
                schedule["tues"][time.time].append(Medication.query.filter_by(med_id=time.medication).first())
            else:
                schedule["tues"][time.time] = [Medication.query.filter_by(med_id=time.medication).first()]
        if time.wed:
            if time.time in schedule["wed"]:
                schedule["wed"][time.time].append(Medication.query.filter_by(med_id=time.medication).first())
            else:
                schedule["wed"][time.time] = [Medication.query.filter_by(med_id=time.medication).first()]
        if time.thur:
            if time.time in schedule["thur"]:
                schedule["thur"][time.time].append(Medication.query.filter_by(med_id=time.medication).first())
            else:
                schedule["thur"][time.time] = [Medication.query.filter_by(med_id=time.medication).first()]
        if time.fri:
            if time.time in schedule["fri"]:
                schedule["fri"][time.time].append(Medication.query.filter_by(med_id=time.medication).first())
            else:
                schedule["fri"][time.time] = [Medication.query.filter_by(med_id=time.medication).first()]
        if time.sat:
            if time.time in schedule["sat"]:
                schedule["sat"][time.time].append(Medication.query.filter_by(med_id=time.medication).first())
            else:
                schedule["sat"][time.time] = [Medication.query.filter_by(med_id=time.medication).first()]
    return schedule
