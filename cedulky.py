import os
import yaml
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    consoles = []
    for filename in os.listdir("consoles"):
        consoles.append(filename.split(".")[0])
    return render_template("index.html",
                           consoles=consoles
                           )


@app.route("/<console>")
def page(console):
    with open(f"consoles/{console}.yaml", encoding="utf-8") as f:
        parameters = yaml.safe_load(f)
    return render_template("RH_Layout.html",
                           **parameters
                           )


app.run(debug=True)
