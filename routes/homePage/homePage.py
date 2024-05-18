from flask import Blueprint, render_template, request

homePage_blueprint = Blueprint('home-page', __name__, template_folder='templates', static_folder='static')

@homePage_blueprint.route('/')
def home_page():
    sidebar_state = request.cookies.get('sidebarState', 'open')
    return render_template('homePage.html')
