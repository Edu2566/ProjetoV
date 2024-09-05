from flask import Blueprint, render_template, send_file
from api.get_vestibulloby_api import get_vestibulloby_api_id, get_vestibulloby_api

colleges_blueprint = Blueprint('colleges', __name__, template_folder='templates', static_folder='static-colleges')

@colleges_blueprint.route('/colleges')
def colleges_menu():
    college_api_data = get_vestibulloby_api()
    
    if college_api_data is None:
        return "Erro ao buscar dados da faculdade", 500
    
    return render_template('colleges-menu.html', college_api_data=college_api_data)


@colleges_blueprint.route('/colleges-information/<int:college_id>')
def college_information(college_id):
    # Faz a requisição para obter os dados da faculdade
    college, error_message, status_code = get_vestibulloby_api_id(college_id)
    
    if college is None:
        return error_message, status_code
    
    # Renderiza o template passando os dados da faculdade específica
    return render_template('colleges-information.html', college=college)

@colleges_blueprint.route('/view-exam')
def view_exam():
    return render_template('view-exam.html')

@colleges_blueprint.route('/pdf')
def pdf():
    return send_file('./pdf/Prova.pdf')