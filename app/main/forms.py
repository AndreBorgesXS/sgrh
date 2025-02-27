from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class UserEditForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Atualizar')

    def __init__(self, user_id=None, **kwargs):
        super(UserEditForm, self).__init__(**kwargs)
        self.user_id = user_id  # Store user ID for validation

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user and user.id != self.user_id:
            raise ValidationError('Este usuário já está registrado')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data.lower()).first()
        if user and user.id != self.user_id:
            raise ValidationError('Este e-mail já está registrado')

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[
        DataRequired(message="E-mail é obrigatório"),
        Email(message="Digite um e-mail válido")
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message="Senha é obrigatória")
    ])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[
        DataRequired(message="Usuário é obrigatório")
    ])
    email = StringField('E-mail', validators=[
        DataRequired(message="E-mail é obrigatório"),
        Email(message="Digite um e-mail válido")
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message="Senha é obrigatória")
    ])
    confirm_password = PasswordField('Confirmar Senha', validators=[
        DataRequired(message="Confirmação de senha é obrigatória"),
        EqualTo('password', message="Senhas não correspondem")
    ])
    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este usuário já está registrado')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data.lower()).first()
        if user:
            raise ValidationError('Este e-mail já está registrado')