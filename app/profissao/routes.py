from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from . import profissao_bp
from app.models import ProfissaoCargo, Pessoa
from .forms import ProfissaoForm
from .. import db
from flask_login import login_required


@profissao_bp.route('/')
@login_required
def index():
    profissoes = ProfissaoCargo.query.all()
    form = ProfissaoForm()  # Create a form instance
    return render_template('profissao/index.html', profissoes=profissoes, form=form)


@profissao_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ProfissaoForm()
    if form.validate_on_submit():
        new_profissao = ProfissaoCargo(cargo=form.cargo.data, pessoa_id=form.pessoa_id.data)
        db.session.add(new_profissao)
        db.session.commit()
        flash('Profissão cadastrada com sucesso!', 'success')
        return redirect(url_for('profissao.index'))
    return render_template('profissao/create.html', form=form)


@profissao_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    profissao = ProfissaoCargo.query.get_or_404(id)
    form = ProfissaoForm(obj=profissao)
    if form.validate_on_submit():
        # Verifica se a nova pessoa_id existe
        new_pessoa = Pessoa.query.get(form.pessoa_id.data)
        if not new_pessoa:
            flash('Pessoa não encontrada. Verifique o ID.', 'error')
            return redirect(url_for('profissao.edit', id=id))
        profissao.cargo = form.cargo.data
        profissao.pessoa_id = form.pessoa_id.data
        db.session.commit()
        flash('Profissão/Cargo atualizada com sucesso!', 'success')
        return redirect(url_for('profissao.index'))
    return render_template('profissao/edit.html', form=form)


@profissao_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    profissao = ProfissaoCargo.query.get_or_404(id)
    db.session.delete(profissao)
    db.session.commit()
    flash('Profissão/Cargo excluída com sucesso.', 'success')
    return redirect(url_for('profissao.index'))