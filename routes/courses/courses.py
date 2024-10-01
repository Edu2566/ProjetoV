from flask import Blueprint, render_template
from api.CollegeAPI import CollegeAPI

college_api_instance = CollegeAPI()

courses_blueprint = Blueprint('courses', __name__, template_folder='templates', static_folder='static-courses')

@courses_blueprint.route('/courses')
def courses_menu():
    college_api_data = college_api_instance.get_all_courses()
    college_api_images = college_api_instance.get_courses_image()

    if 'error' in college_api_data or 'error' in college_api_images:
        return "Erro ao buscar dados da faculdade", 500

    images_map = {image['science_type']: image['course_image_url'] for image in college_api_images}

    return render_template('courses-menu.html', college_api_data=college_api_data, images_map=images_map)
