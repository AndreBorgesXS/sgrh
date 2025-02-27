from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://openpg:openpgpwd@localhost/sgrh'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from app.main import main_bp
        from app.pessoa import pessoa_bp
        from app.profissao import profissao_bp
        from app.folha import folha_bp
        from app.capacitacao import capacitacao_bp

        app.register_blueprint(main_bp, url_prefix='/')
        app.register_blueprint(pessoa_bp, url_prefix='/pessoa')
        app.register_blueprint(profissao_bp, url_prefix='/profissao')
        app.register_blueprint(folha_bp, url_prefix='/folha')
        app.register_blueprint(capacitacao_bp, url_prefix='/capacitacao')

        return app
