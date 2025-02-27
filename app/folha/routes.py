from flask import render_template, redirect, url_for, flash, request

from . import folha_bp
from .forms import FolhaForm
from ..models import FolhaPagamento
from .. import db, main
from flask_login import login_required, current_user, login_user
from app.main.forms import LoginForm
from app.models import User



# CRUD para Folha de Pagamento
@folha_bp.route('/', methods=['GET'])
@login_required
def index():
    folhas = FolhaPagamento.query.all()
    return render_template('folha/index.html', folhas=folhas, user=current_user)


@folha_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = FolhaForm()
    if form.validate_on_submit():
        # Cria nova folha de pagamento
        new_folha = FolhaPagamento(
            valor=form.valor.data,
            data_pgto=form.data_pgto.data,
            pessoa_id=form.pessoa_id.data
        )
        db.session.add(new_folha)
        db.session.commit()
        flash('Folha de pagamento criada com sucesso!', 'success')
        return redirect(url_for('folha.index'))
    return render_template('folha/create.html', form=form, user=current_user)


@folha_bp.route('/<int:id>', methods=['GET'])
@login_required
def view(id):
    folha = FolhaPagamento.query.get_or_404(id)
    return render_template('folha/view.html', folha=folha, user=current_user)


@folha_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    folha = FolhaPagamento.query.get_or_404(id)
    form = FolhaForm(obj=folha)

    if form.validate_on_submit():
        # Atualiza a folha de pagamento
        folha.valor = form.valor.data
        folha.data_pgto = form.data_pgto.data
        folha.pessoa_id = form.pessoa_id.data
        db.session.commit()
        flash('Folha de pagamento atualizada!', 'success')
        return redirect(url_for('folha.view', id=folha.id))

    return render_template('folha/edit.html', form=form, folha=folha, user=current_user)


@folha_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    folha = FolhaPagamento.query.get_or_404(id)
    db.session.delete(folha)
    db.session.commit()
    flash('Folha de pagamento deletada!', 'success')
    return redirect(url_for('folha.index'))