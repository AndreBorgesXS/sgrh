from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class ProfissaoForm(FlaskForm):
    cargo = StringField('Cargo', validators=[DataRequired()])
    pessoa_id = IntegerField('ID da Pessoa', validators=[DataRequired()])
    submit = SubmitField('Salvar')