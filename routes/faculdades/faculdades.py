from flask import Blueprint, render_template

faculdades_blueprint = Blueprint('faculdades', __name__, template_folder='templates', static_folder='static')

@faculdades_blueprint.route('/faculdades')
def faculdades_menu():
    return render_template('faculdadesMenu.html')
