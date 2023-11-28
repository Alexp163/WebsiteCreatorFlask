from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(8, 32)])


class RegisterForm(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired(), Email()])
    password_1 = PasswordField("Пароль", validators=[DataRequired(), Length(8, 32)])
    password_2 = PasswordField("Пароль", validators=[DataRequired(), Length(8, 32)])

    def are_password_equal(self):
        pass
