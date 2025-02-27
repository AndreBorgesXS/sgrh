from flask import Blueprint

profissao_bp = Blueprint('profissao', __name__, template_folder='templates', url_prefix='/profissao')

from . import routes