from flask_wtf import FlaskForm
from wtforms import FloatField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError

class FolhaForm(FlaskForm):
    valor = FloatField('Valor RS', validators=[
        DataRequired(),
        NumberRange(min=0, max=50000, message='Valor deve estar entre 0 e 50000')
    ])
    data_pgto = DateField('Data de Pagamento', validators=[DataRequired()])
    pessoa_id = IntegerField('ID da Pessoa', validators=[DataRequired()])
    submit = SubmitField('Salvar')