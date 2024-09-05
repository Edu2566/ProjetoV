from flask import Blueprint, render_template

courses_blueprint = Blueprint('courses', __name__, template_folder='templates', static_folder='static-courses')

@courses_blueprint.route('/courses')
def courses_menu():
    return render_template('courses-menu.html')