from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length


class PessoaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired()])
    submit = SubmitField('Salvar')