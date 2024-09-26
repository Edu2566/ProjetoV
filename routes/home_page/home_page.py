# home_page.py
from flask import Blueprint, render_template
from api.CollegeAPI import CollegeAPI

# Inicializando a API
college_api_instance = CollegeAPI()

home_page_blueprint = Blueprint('home-page', __name__, static_folder='static-home', template_folder='templates')

@home_page_blueprint.route('/')
def home_page():
    # Requisição para obter todos os dados das faculdades
    college_api_data = college_api_instance.get_all_colleges()
    college_api_course = college_api_instance.get_all_courses()
    
    if 'error' in college_api_data or 'error' in college_api_course:
        return "Erro ao buscar dados.", 500
    
    return render_template('home_page.html', college_api_data=college_api_data, college_api_course=college_api_course)
