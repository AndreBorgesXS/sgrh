from flask import Blueprint

pessoa_bp = Blueprint('pessoa', __name__, template_folder='templates', url_prefix='/pessoa')

from . import routes  # Importa rotas deste blueprint