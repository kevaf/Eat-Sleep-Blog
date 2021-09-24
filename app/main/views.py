from flask import render_template, request, redirect, url_for,abort,flash
from . import main
from .froms import UpdateProfile
from .. import db, photos
from ..models import User, Comment, Blog, Subscriber
from flask_login import login_required, current_user
from ..requests import get_blogQuotes
from ..email import mail_message

#views
@main.route('/')
def index():
    """
    view root page function that returns index page
    """

@main.route('/home')
def home():
    blogQuote = get_blogQuotes()

    title = 'Eat-Sleep_Blog'
    return render_template('home.html', title=title, blogQuote=blogQuote)
    
