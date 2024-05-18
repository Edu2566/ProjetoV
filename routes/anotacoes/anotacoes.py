from flask import Blueprint, render_template

anotacoes_blueprint = Blueprint('anotacoes', __name__, template_folder='templates', static_folder='static')

@anotacoes_blueprint.route('/anotacoes')
def anotacoes_menu():
    return render_template('anotacoesMenu.html')