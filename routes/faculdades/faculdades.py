import requests
from flask import Blueprint, render_template

faculdades_blueprint = Blueprint('faculdades', __name__, template_folder='templates', static_folder='static-faculdades')

@faculdades_blueprint.route('/faculdades')
def faculdades_menu():
    return render_template('faculdadesMenu.html')

@faculdades_blueprint.route('/faculty-information/<int:faculty_id>')
def faculty_information(faculty_id):
    # Faz a requisição para obter os dados da faculdade com o ID fornecido
    response_faculty = requests.get("https://c3e1bccd-e40f-4642-a5e0-6b45d108af4b-00-3g9s82kxsdncm.picard.replit.dev/")
    faculty_data = response_faculty.json()  # Recebe os dados da API

    # Filtra a faculdade específica com base no ID
    faculty = next((f for f in faculty_data if f["id_faculdade"] == faculty_id), None)
    
    if faculty is None:
        return "Faculdade não encontrada", 404

    response_courses = requests.get("https://c3e1bccd-e40f-4642-a5e0-6b45d108af4b-00-3g9s82kxsdncm.picard.replit.dev/courses")
    courses_data = response_courses.json()

    cursos = [course['nome_curso'] for course in courses_data if course['id_faculdade'] == faculty_id]
    
    # Adiciona a lista de cursos ao dicionário da faculdade
    faculty['cursos'] = cursos
    
    # Renderiza o template passando os dados da faculdade específica
    return render_template('faculty-information.html', faculty=faculty)

