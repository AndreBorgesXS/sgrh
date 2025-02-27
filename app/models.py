import datetime
from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# MODELO DE USUÁRIO (AUTENTICAÇÃO)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# MODELO DE PESSOA
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)



# MODELO DE PROFISSAO/CARGO
class ProfissaoCargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(100), nullable=False)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)


# MODELO DE FOLHA DE PAGAMENTO
class FolhaPagamento(db.Model):
    __tablename__ = 'folha_pagamento'
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    data_pgto = db.Column(db.Date, default=datetime.date)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)


# MODELO DE CAPACITACAO
class Capacitacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    data_conclusao = db.Column(db.Date)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    pessoa = db.relationship('Pessoa', backref=db.backref('capacitacoes', lazy=True))