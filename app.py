from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_data = [
        {
            'title': 'Portfolio Website',
            'description': 'A responsive personal portfolio built with Flask',
            'technologies': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript'],
            'github_link': 'https://github.com/mfza0/Portfolio'
        },
        {
            'title': 'Web Development Projects',
            'description': 'Collection of web development projects using modern technologies',
            'technologies': ['HTML', 'CSS', 'JavaScript'],
            'github_link': '#'
        },
        {
            'title': 'Python Learning Projects',
            'description': 'Various Python projects demonstrating different concepts',
            'technologies': ['Python', 'Flask'],
            'github_link': '#'
        }
    ]
    return render_template('projects.html', projects=projects_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        if not name or not email or not message:
            flash('Please fill in all fields.', 'error')
            return render_template('contact.html')
        
        flash(f'Thank you {name}! Your message has been received. I\'ll get back to you soon!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)