import os
from flask_optimize import FlaskOptimize
from flask import render_template, Flask

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

flask_optimize = FlaskOptimize()

# Get app config from absolute file path
if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

@app.route("/", methods=["GET"])
@flask_optimize.optimize()
def home():
    return render_template("index.html")