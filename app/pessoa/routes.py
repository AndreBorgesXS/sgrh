from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from app.models import db, Pessoa
from app.pessoa.forms import PessoaForm
from . import pessoa_bp
from flask_login import login_required

@pessoa_bp.route('/')
@login_required
def index():
    pessoas = Pessoa.query.all()
    return render_template('pessoa/index.html', pessoas=pessoas)


@pessoa_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PessoaForm()
    if form.validate_on_submit():
        pessoa = Pessoa()
        form.populate_obj(pessoa)
        db.session.add(pessoa)
        db.session.commit()
        flash('Pessoa criada com sucesso!', 'success')
        return redirect(url_for('pessoa.index'))
    return render_template('pessoa/create.html', form=form, create=True)


@pessoa_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    pessoa = Pessoa.query.get_or_404(id)
    form = PessoaForm(obj=pessoa)
    if form.validate_on_submit():
        form.populate_obj(pessoa)
        db.session.commit()
        flash('Pessoa atualizada com sucesso!', 'success')
        return redirect(url_for('pessoa.index'))
    return render_template('pessoa/edit.html', form=form, pessoa=pessoa)


@pessoa_bp.route('/view/<int:id>')
@login_required
def view(id):
    pessoa = Pessoa.query.get_or_404(id)
    return render_template('pessoa/view.html', pessoa=pessoa)


@pessoa_bp.route('/delete/<int:id>', methods=['DELETE'])
@login_required
def delete(id):
    pessoa = Pessoa.query.get_or_404(id)
    try:
        db.session.delete(pessoa)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Pessoa excluída com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'Erro ao excluir pessoa!'}), 400
