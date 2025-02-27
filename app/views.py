from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Abishua Johnson")

@app.route('/profile')
def profile():
    """Render the website's profile page."""
    date_joined = datetime.date(2023, 2, 15)
    formatted_date = format_date_joined(date_joined)
    
    return render_template('profile.html', 
                          date_joined=formatted_date,
                          username="abishua",
                          name="Abishua Johnson",
                          location="Kingston, Jamaica",
                          bio="Computer Science student with a passion for web development and AI. I love building things that live on the internet :)",
                          posts=15,
                          followers=175000,
                          following=1)

def format_date_joined(date):
    """Format the date to return only month and year."""
    return date.strftime("%B, %Y")

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404