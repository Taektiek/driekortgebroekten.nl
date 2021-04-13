from flask import render_template
from app import app

# In de view functie moet je aangeven welk deel van de navbar actief is. Dat doe je zo:
# render_template("...html", naamvanonderdeel="active")

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", blog="active")