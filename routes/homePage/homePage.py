from flask import Blueprint, render_template, request
from api.get_vestibulloby_api import get_vestibulloby_api

homePage_blueprint = Blueprint('home-page', __name__, static_folder='static-home', template_folder='templates')

@homePage_blueprint.route('/')
def home_page():
    faculty_api_data = get_vestibulloby_api()
    
    if faculty_api_data is None:
        return "Erro ao buscar dados da faculdade", 500
    
    return render_template('homePage.html', faculty_api_data=faculty_api_data)
