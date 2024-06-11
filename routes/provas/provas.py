from flask import Blueprint, render_template

provas_blueprint = Blueprint('provas', __name__, static_folder='static-provas', template_folder='templates')

@provas_blueprint.route('/provas')
def provas_menu():
    return render_template('provasMenu.html')