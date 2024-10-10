from flask import Blueprint, render_template
from api.CollegeAPI import CollegeAPI

college_api_instance = CollegeAPI()

home_page_blueprint = Blueprint('home-page', __name__, static_folder='static-home', template_folder='templates')

@home_page_blueprint.route('/')
def home_page():
    college_api_data = college_api_instance.get_all_colleges()
    
    if 'error' in college_api_data:
        return "Erro ao buscar dados.", 500
    
    return render_template('home-page.html', college_api_data=college_api_data)
