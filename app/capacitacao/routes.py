from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required

from . import capacitacao_bp
from .forms import CapacitacaoForm
from ..models import Capacitacao
from .. import db

login_redirect = 'main.dashboard'


@capacitacao_bp.route('/')
@login_required
def index():
    capacitacoes = Capacitacao.query.all()
    return render_template('capacitacao/index.html', capacitacoes=capacitacoes)


@capacitacao_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CapacitacaoForm()
    if form.validate_on_submit():
        new_capacitacao = Capacitacao(
            tipo=form.tipo.data,
            data_conclusao=form.data_conclusao.data,
            pessoa_id=form.pessoa_id.data
        )
        db.session.add(new_capacitacao)
        db.session.commit()
        flash('Capacitação registrada com sucesso!', 'success')
        return redirect(url_for('capacitacao.index'))
    return render_template('capacitacao/create.html', form=form)


@capacitacao_bp.route('/<int:id>')
@login_required
def view(id):
    capacitacao = Capacitacao.query.get_or_404(id)
    return render_template('capacitacao/view.html', capacitacao=capacitacao)


@capacitacao_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    capacitacao = Capacitacao.query.get_or_404(id)
    form = CapacitacaoForm(obj=capacitacao)

    if form.validate_on_submit():
        capacitacao.tipo = form.tipo.data
        capacitacao.data_conclusao = form.data_conclusao.data
        capacitacao.pessoa_id = form.pessoa_id.data
        db.session.commit()
        flash('Capacitação atualizada com sucesso!', 'success')
        return redirect(url_for('capacitacao.index'))

    return render_template('capacitacao/edit.html', form=form)


@capacitacao_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    capacitacao = Capacitacao.query.get_or_404(id)
    db.session.delete(capacitacao)
    db.session.commit()
    flash('Capacitação excluída.', 'success')
    return redirect(url_for('capacitacao.index'))