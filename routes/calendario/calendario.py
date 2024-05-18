from flask import Blueprint, render_template

calendario_blueprint = Blueprint('calendario', __name__, template_folder='templates', static_folder='static')

@calendario_blueprint.route('/calendario')
def calendario_menu():
    return render_template('calendarioMenu.html')