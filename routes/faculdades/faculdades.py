from flask import Blueprint, render_template
from api.get_vestibulloby_api import get_vestibulloby_api_id, get_vestibulloby_api

faculdades_blueprint = Blueprint('faculdades', __name__, template_folder='templates', static_folder='static-faculdades')

@faculdades_blueprint.route('/faculdades')
def faculdades_menu():
    faculty_api_data = get_vestibulloby_api()
    
    if faculty_api_data is None:
        return "Erro ao buscar dados da faculdade", 500
    
    return render_template('faculdadesMenu.html', faculty_api_data=faculty_api_data)


@faculdades_blueprint.route('/faculty-information/<int:faculty_id>')
def faculty_information(faculty_id):
    # Faz a requisição para obter os dados da faculdade
    faculty, error_message, status_code = get_vestibulloby_api_id(faculty_id)
    
    if faculty is None:
        return error_message, status_code
    
    # Renderiza o template passando os dados da faculdade específica
    return render_template('faculty-information.html', faculty=faculty)

