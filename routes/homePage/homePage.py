from flask import Blueprint, render_template, request

homePage_blueprint = Blueprint('home-page', __name__, static_folder='static-home', template_folder='templates')

@homePage_blueprint.route('/')
def home_page():
    return render_template('homePage.html')
