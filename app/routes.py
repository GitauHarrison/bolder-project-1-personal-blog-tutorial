from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html', title = 'About Me')


@app.route('/hire-me')
def hire_me():
    return render_template('hire_me.html', title = 'Hire Me')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title = 'Portfolio')

@app.route('/my-interests')
def my_interests():
    return render_template('my_interests.html', title = 'My Interests')