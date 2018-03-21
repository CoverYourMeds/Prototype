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
from CoverYourMeds.models import Medication


@app.route("/", methods=["GET"])
def home():
    db.create_all()
    return render_template("index.html")


@app.route("/mymeds", methods=["GET"])
def mymeds():
    db.create_all()

    # Grab all medications from database
    medications = Medication.query.all()
    return render_template("mymeds.html", medications=medications)


@app.route("/settings", methods=["GET"])
def settings():
    return render_template("settings.html")
