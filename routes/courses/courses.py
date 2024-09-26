from flask import Blueprint, render_template
from api.CollegeAPI import CollegeAPI

college_api_instance = CollegeAPI()

courses_blueprint = Blueprint('courses', __name__, template_folder='templates', static_folder='static-courses')

@courses_blueprint.route('/courses')
def courses_menu():
    college_api_data = college_api_instance.get_all_courses()
    
    if 'error' in college_api_data:
        return "Erro ao buscar dados da faculdade", 500
    
    return render_template('courses-menu.html', college_api_data=college_api_data)