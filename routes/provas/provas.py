from flask import Blueprint, render_template

provas_blueprint = Blueprint('provas', __name__, template_folder='templates', static_folder='static')

@provas_blueprint.route('/provas')
def provas_menu():
    return render_template('provasMenu.html')