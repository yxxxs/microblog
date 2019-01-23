from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('USERNAME', validators=[DataRequired()])
    password = PasswordField('PASSWORD', validators=[DataRequired()])
    remember_me = BooleanField('REMEMBER ME')
    submit = SubmitField('SIGH IN')