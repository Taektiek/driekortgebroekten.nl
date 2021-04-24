from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Gebruikersnaam', validators=[DataRequired()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    remember_me = BooleanField('Onthoud mij')
    submit = SubmitField('Log in')

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Ondertitel')
    summary = TextAreaField('Samenvatting', validators=[DataRequired(), Length(min=1, max=1028)])
    body = TextAreaField('Artikel', validators=[DataRequired()])
    submit = SubmitField('Voeg toe')