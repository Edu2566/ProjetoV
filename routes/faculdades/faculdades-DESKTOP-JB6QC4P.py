import requests
from flask import Blueprint, render_template

faculdades_blueprint = Blueprint('faculdades', __name__, template_folder='templates', static_folder='static-faculdades')

@faculdades_blueprint.route('/faculdades')
def faculdades_menu():
    return render_template('faculdadesMenu.html')

@faculdades_blueprint.route('/faculty-information/<int:faculdade_id>')
def faculty_information(faculdade_id):
    # Faz a requisição para obter os dados da faculdade com o ID fornecido
    response = requests.get("https://f839e9a8-9bc7-43c5-83ac-49861251fa78-00-gfzzlif47had.worf.replit.dev/")
    faculty_data = response.json()  # Recebe os dados da API

    # Filtra a faculdade específica com base no ID
    faculty_data = next((f for f in faculty_data if f["id_faculdade"] == faculdade_id), None)

    if faculty_data is None:
        return "Faculdade não encontrada", 404

    # Renderiza o template passando os dados da faculdade específica
    return render_template('faculty-information.html', faculty_data=faculty_data)

