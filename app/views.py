from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime  # Added for date handling

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
    return render_template('about.html', name="Mary Jane")


@app.route('/profile')
def profile():
    """Render the fake profile page."""
    date_joined = datetime.date(2019, 2, 7)
    formatted_date = format_date_joined(date_joined)
    
    profile_data = {
        'full_name': 'Abishua S. Johnson',           
        'username': 'abishua',             
        'location': 'Kingston, Jamaica',       
        'date_joined': formatted_date,
        'bio': 'I am a final year Computer Science major who is passionate about Artificial Intelligence and Machine Learning.',
        'posts': 10,
        'followers': 7560789,
        'following': 0,
        'image': 'abishua.jpg'    
    }
    
    return render_template('profile.html', profile=profile_data)


def format_date_joined(date_joined):
    """Formats a date object into 'Month, Year' format."""
    return date_joined.strftime("%B, %Y")


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to force the latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
