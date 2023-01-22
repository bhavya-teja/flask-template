from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/ark')
def ark():
    return render_template('ark.html')

@bp.route('/projects')
def projects():
    return render_template('projects.html')

@bp.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@bp.route('/error')
def error():
    return render_template('error.html')