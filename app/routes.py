from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, WriteArticleForm
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Article
from werkzeug.urls import url_parse
from markdown import markdown

# In de view functie moet je aangeven welk deel van de navbar actief is. Dat doe je zo:
# render_template("...html", naamvanonderdeel="active")

@app.route('/')
@app.route('/index')
def index():
    bannerarticle = Article.query.order_by(Article.timestamp.desc()).first()
    articles = Article.query.order_by(Article.timestamp.desc()).all()[1:]
    return render_template("index.html", title='Blog', blogclass="active", bannerarticle=bannerarticle, articles=articles)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Het ingevulde e-mailadres of wachtwoord is ongeldig.', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", title='Inloggen', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/podcast')
def podcast():
    return render_template("podcasts.html", title='Podcasts', podcastclass="active")

@app.route('/boekenclub')
def boekenclub():
    return render_template("boekenclub.html", title='Boekenclub', boekenclubclass="active")

@app.route('/article/<url>')
def article(url):
    article = Article.query.filter_by(url=url).first()
    return render_template("article.html", blogclass="active", article=article, markdown=markdown(article.body))

@app.route('/voegtoe', methods=['GET', 'POST'])
@login_required
def voegtoe():
    form = WriteArticleForm()
    if form.validate_on_submit():
        article = Article(title=form.title.data, subtitle=form.subtitle.data,
                          summary=form.summary.data, body=form.body.data,
                          author=current_user, url=form.url.data)
        db.session.add(article)
        db.session.commit()
        flash('Het artikel is gepubliceerd!', 'success')
        return redirect(url_for('index'))
    return render_template('artikelschrijven.html', blogclass="active", title='Artikel toevoegen', form=form)