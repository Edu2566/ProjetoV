from flask import Blueprint, render_template

notificacoes_blueprint = Blueprint('notificacoes', __name__, template_folder='templates', static_folder='static-notificacoes')

@notificacoes_blueprint.route('/notificacoes')
def notificacoes_menu():
    return render_template('notificacoesMenu.html')