from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.dynamodb import users_table
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        response = users_table.get_item(Key={'email': email})
        user = response.get('Item')

        if user and user['password'] == password:
            session['user_email'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        response = users_table.get_item(Key={'email': email})
        if 'Item' in response:
            flash('Email already registered', 'warning')
            return redirect(url_for('auth.register'))

        users_table.put_item(
            Item={
                'email': email,
                'name': name,
                'password': password,
                'created_at': datetime.utcnow().isoformat()
            }
        )

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user_email', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
