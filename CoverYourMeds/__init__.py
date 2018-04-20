import os

from flask import render_template, Flask, make_response, redirect, request
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
from CoverYourMeds.models import Medication, Times, User, Doctor


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        print(request.method)
        return render_template("login.html")
    else:
        print(request.method)
        username = request.form['email']
        user = User.query.filter_by(username=username).first()
        resp = make_response(redirect("/"))
        if user.password == request.form['password']:
            resp.set_cookie('user', username)
        else:
            resp.set_cookie('user', username, expires=0)
        return resp


@app.route("/logout", methods=["GET"])
def logout():
    resp = make_response(redirect("/"))
    resp.set_cookie('user', '', expires=0)
    return resp


@app.route("/", methods=["GET"])
def home():
    if request.cookies.get('user'):
        db.create_all()
        curUser=User.query.filter_by(username=request.cookies.get('user')).first()
        if curUser.type=='caretaker':
            medUserList=User.query.filter_by(type='user').all()

            return render_template("base.html",medUserList=medUserList)
        else:
            times = Times.query.all()
            schedule = make_schedule(times)
            doctors = Doctor.query.all()
            return render_template("index.html", schedule=schedule, doctors=doctors)
    return redirect("/login")


@app.route("/mymeds", methods=["GET"])
def mymeds():
    if request.cookies.get('user'):
        db.create_all()

        # Grab all medications from database
        medications = Medication.query.all()
        doctors = Doctor.query.all()
        return render_template("mymeds.html", medications=medications, doctors=doctors)
    return redirect("/login")


@app.route("/newMed", methods=["POST"])
def newMed():
    if request.cookies.get('user'):
        data = request.form
        newMedication = Medication(data['med-name'], data['pills'], data['refill_date'], data['doc_id'],
                                   request.cookies.get('user'))
        db.session.add(newMedication)
        db.session.commit()
        return redirect("/")
    return redirect("/login")


@app.route("/newDoc", methods=["POST"])
def newDoc():
    if request.cookies.get('user'):
        data = request.form
        newDoctor = Doctor(data['doc-name'])
        db.session.add(newDoctor)
        db.session.commit()
        return redirect("/")
    return redirect("/login")

@app.route("/mydocs", methods=["GET"])
def mydocs():
    if request.cookies.get('user'):
        db.create_all()
        doctors = Doctor.query.all()
        medications = Medication.query.all()
        return render_template("mydocs.html", doctors=doctors, medications=medications)
    return redirect("/login")


@app.route("/settings", methods=["GET"])
def settings():
    if request.cookies.get('user'):
        doctors = Doctor.query.all()
        return render_template("settings.html", doctors=doctors)
    return redirect("/login")


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
