from flask import Blueprint

capacitacao_bp = Blueprint(
    'capacitacao',
    __name__,
    template_folder='templates',
    url_prefix='/capacitacao'
)

from . import routes