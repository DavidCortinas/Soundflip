from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models import Post, User
from flask_login import login_user, logout_user

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        p = Post(email='dcortinas33@gmail.com', body=request.form.get('post'))
        db.session.add(p)
        db.session.commit()
        flash('Post created successfully!')
        return redirect(url_for('index'))
    return render_template('index.html', title='Home')

@app.route('/contact')
def contact():
    context = {
        'help': 'yes',
        'page': 1
    }
    return render_template('contact.html', **context)

@app.route('/blog')
def blog():
    context = {
        'posts': [p.to_dict() for p in Post.query.all()]
    }
    return render_template('blog.html', **context, page=1)
    # OR if not using **context in return statement, use 
    # posts=[p1.to_dict(), p2.to_dict(), p3.to_dict()]

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is None or not user.check_password(request.form.get('password')):
            flash('Username or password is incorrect. Try again.')
            return redirect(url_for('login'))
        remember_me = True if request.form.get('checked') is not None else False
        login_user(user, remember=remember_me)
        flash(f'Welcome, {user.first_name} {user.last_name}! You have successfully logged in.')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        u = User()
        u.from_dict(request.form)
        u.save()
        flash('Post created successfully!')
        return redirect(url_for('login'))
    return render_template('register.html')