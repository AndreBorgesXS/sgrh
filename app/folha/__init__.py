from flask import Blueprint

# Cria o Blueprint para Folha de Pagamento
folha_bp = Blueprint(
    'folha',
    __name__,
    template_folder='templates',
    url_prefix='/folha'
)

# Importe as rotas após a criação do Blueprint
from . import routes