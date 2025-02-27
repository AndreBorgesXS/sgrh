from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegistrationForm, UserEditForm
from ..models import User
from .. import db
from . import main_bp


@main_bp.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('main/home.html')

@main_bp.route('/user_management')
@login_required
def user_management():
    users = User.query.all()
    return render_template('main/user_management.html', users=users)


@main_bp.route('/edit_user/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    user = User.query.get_or_404(id)
    form = UserEditForm(user_id=user.id, obj=user)

    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data.lower()
        db.session.commit()
        flash('Usuário atualizado com sucesso!', 'success')
        return redirect(url_for('main.user_management'))

    return render_template('main/edit_user.html', form=form, user=user)


@main_bp.route('/delete_user/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuário excluído com sucesso.', 'success')
    return redirect(url_for('main.user_management'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Credenciais inválidas!', 'danger')

    return render_template('main/login.html', form=form)


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data.lower()
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('main.login'))

    return render_template('main/register.html', form=form)


@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html')