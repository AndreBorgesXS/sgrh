from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Optional

class CapacitacaoForm(FlaskForm):
    tipo = StringField('Tipo de Capacitação', validators=[InputRequired()])
    data_conclusao = DateField('Data de Conclusão', validators=[Optional()])
    pessoa_id = IntegerField('ID da Pessoa', validators=[InputRequired()])
    submit = SubmitField('Salvar')