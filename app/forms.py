from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms_validators import AlphaDash
from app.models import Article


class LoginForm(FlaskForm):
    username = StringField('Gebruikersnaam', validators=[DataRequired(message="Dit veld is noodzakelijk")])
    password = PasswordField('Wachtwoord', validators=[DataRequired(message="Dit veld is noodzakelijk")])
    remember_me = BooleanField('Onthoud mij')
    submit = SubmitField('Log in')


class WriteArticleForm(FlaskForm):
    title = StringField('Titel', validators=[DataRequired(message="Dit veld is noodzakelijk")], default="Titel...")
    # url = StringField('URL', validators=[DataRequired(),
    #                                      AlphaDash(message="De url mag alleen maar tekst en streepjes bevatten")])
    subtitle = StringField('Ondertitel', default="Ondertitel...")
    summary = TextAreaField('Samenvatting', validators=[DataRequired(message="Dit veld is noodzakelijk"), Length(min=1, max=1028)],
                            default="Samenvatting...")
    body = TextAreaField('Artikel', validators=[DataRequired(message="Dit veld is noodzakelijk")], default="Artikel...")
    submit = SubmitField('Voeg toe')

    def validate_title(self, title):
        article = Article.query.filter_by(title=title.data).first()
        if article is not None:
            raise ValidationError("Er bestaat al een artikel met deze titel, kies een andere titel")

    # def validate_url(self, url):
    #     article = Article.query.filter_by(url=url.data).first()
    #     if article is not None:
    #         raise ValidationError("Er bestaat al een artikel met deze url, kies een andere url")
