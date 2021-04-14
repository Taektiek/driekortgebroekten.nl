from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# In de view functie moet je aangeven welk deel van de navbar actief is. Dat doe je zo:
# render_template("...html", naamvanonderdeel="active")

@app.route('/')
@app.route('/index')
def index():
    bannerarticle = {"title": "Ischa’s scheerroutine", "author": "Ischa Sachs", "date": "07/03/2021","summary": "Het scheren van een baard is niet zo makkelijk als je misschien denkt, in zijn dagelijkse blog laat Ischa zien hoe hij te werk gaat. In zijn eerste artikel bespreekt hij zijn routine..."}
    articles = [{"title": "Hoe ‘The Stand’ ons een les kan geven over klimaatverandering", "author": "Taeke Roukema", "date": "12/04/2021",
                 "summary": "‘The Stand’ van Stephen King gaat over een virus die de wereld overgaat en de chaos die daardoor volgt. Velen hebben het daarom al gekoppeld met de huidige coronacrisis. Maar wat zegt het boek over klimaatverandering en kunnen we daar ook iets van leren?"},
                {"title": "Wat betekent basisinkomen voor de gemiddelde lesbische man?", "author": "Riemer Kerkstra",
                 "date": "05/04/2021",
                 "summary": "Binnen linkse kringen is het basisinkomen al jaren een populair idee. Maar wat betekent het nou eigenlijk voor mij, de gemiddelde lesbische man?"},
                {"title": "Wat betekent basisinkomen voor de gemiddelde lesbische man?", "author": "Riemer Kerkstra",
                 "date": "05/04/2021",
                 "summary": "Binnen linkse kringen is het basisinkomen al jaren een populair idee. Maar wat betekent het nou eigenlijk voor mij, de gemiddelde lesbische man?"}
                ]
    return render_template("index.html", blog="active", bannerarticle=bannerarticle, articles=articles)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login aangevraagd voor gebruiker {}, onthoud_mij={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", form=form)