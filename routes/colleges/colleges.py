# colleges.py
from flask import Blueprint, render_template, url_for
from api.get_vestibulloby_api import CollegeAPI  # Importando a classe da nova API

# Inicializando a API
college_api_instance = CollegeAPI()

colleges_blueprint = Blueprint('colleges', __name__, template_folder='templates', static_folder='static-colleges')

@colleges_blueprint.route('/colleges-information/<int:college_id>')
def college_information(college_id):
    # Faz a requisição para obter os dados da faculdade específica
    college_data = college_api_instance.get_college_by_id(college_id)
    
    if 'error' in college_data:
        return college_data['error'], 404
    
    # Renderiza o template passando os dados da faculdade específica
    return render_template('colleges-information.html', college=college_data)

@colleges_blueprint.route('/view-exam/<int:exam_id>')
def view_exam(exam_id):
    # Obtenha os detalhes do exame a partir do ID
    exam_data = college_api_instance.get_exam_by_id(exam_id)
    
    if 'error' in exam_data:
        return exam_data['error'], 404
    
    # Verifica se o valor de 'exam_pdf' é uma URL completa ou apenas o nome do arquivo
    pdf_url = exam_data["exam_pdf_url"]

    # Renderize o template passando a URL do PDF
    return render_template('view-exam.html', pdf_url=pdf_url)



