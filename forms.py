from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()], render_kw={ "placeholder": "John Doe" })
  email = StringField('Email', validators=[DataRequired(), Email(message=('Not a valid email address'))], render_kw={ "placeholder": "johndoe@gmail.com" })
  message = TextAreaField('Message', validators=[DataRequired()], render_kw={ "placeholder": "Write your question / message..." })
  # recaptcha = RecaptchaField()
  submit = SubmitField('Submit')