import re
import os
import yaml
from markupsafe import Markup
# from flask import Flask, render_template, Markup
from flask import Flask, render_template
from flaskext.markdown import Markdown

app = Flask(__name__)
markdown = Markdown(app)

@app.template_filter('fix_spaces')
def fix_spaces(text):
    text = re.sub("(\d) ", "\\1\u00a0", text)
    return text

def get_consoles():
    consoles = []
    for filename in os.listdir("consoles"):
        consoles.append(filename.split(".")[0])
    
    consoles.sort(key=lambda x: x.lower())

    return consoles

@app.route("/")
def index():
    consoles = get_consoles()

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


app.run(port=8099, debug=True)
