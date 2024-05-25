from flask import Blueprint, render_template

configuracoes_blueprint = Blueprint('configuracoes', __name__, template_folder='templates', static_folder='static-configuracoes')

@configuracoes_blueprint.route('/configuracoes')
def configuracoes_menu():
    return render_template('configuracoesMenu.html')