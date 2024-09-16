# home_page.py
from flask import Blueprint, render_template
from api.get_vestibulloby_api import CollegeAPI

# Inicializando a API
college_api_instance = CollegeAPI()

home_page_blueprint = Blueprint('home-page', __name__, static_folder='static-home', template_folder='templates')

@home_page_blueprint.route('/')
def home_page():
    # Requisição para obter todos os dados das faculdades
    college_api_data = college_api_instance.get_all_colleges()
    
    if 'error' in college_api_data:
        return "Erro ao buscar dados da faculdade", 500
    
    return render_template('home_page.html', college_api_data=college_api_data)
