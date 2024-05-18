from flask import Blueprint, render_template

cursos_blueprint = Blueprint('cursos', __name__, template_folder='templates', static_folder='static')

@cursos_blueprint.route('/cursos')
def cursos_menu():
    return render_template('cursosMenu.html')