from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import login_user, logout_user
from app.models import User

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
    return render_template("index.html", blogclass="active", bannerarticle=bannerarticle, articles=articles)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Het ingevulde e-mailadres of wachtwoord is ongeldig.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/podcast')
def podcast():
    return render_template("podcasts.html", podcastclass="active")

@app.route('/boekenclub')
def boekenclub():
    return render_template("boekenclub.html", boekenclubclass="active")

@app.route('/thestand-210412')
def thestand():
    return render_template("thestand.html", blogclass="active")