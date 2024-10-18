from flask import Blueprint, render_template, request, jsonify
import json

notes_blueprint = Blueprint('notes', __name__, template_folder='templates', static_folder='static-notes')
FILE_PATH = 'notebooks_data.json'

# Funções para manipulação de cadernos
def load_notebooks():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            notebooks = json.load(file)
    except FileNotFoundError:
        notebooks = []
    return notebooks

def save_notebooks(notebooks):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(notebooks, file, ensure_ascii=False, indent=4)

@notes_blueprint.route('/notes')
def notes_menu():
    return render_template('notes-menu.html', notebooks=load_notebooks())

@notes_blueprint.route('/notes/<notebook_name>')
def view_notebook(notebook_name):
    return render_template('view-notebook.html', notebook_name=notebook_name)

@notes_blueprint.route('/notes/add', methods=['POST'])
def add_notebook():
    notebook_name = request.json.get('name')
    if notebook_name:
        notebooks = load_notebooks()
        if notebook_name not in notebooks:
            notebooks.append(notebook_name)
            save_notebooks(notebooks)
            return jsonify({"success": True, "notebooks": notebooks}), 201
    return jsonify({"success": False}), 400

@notes_blueprint.route('/notes/edit', methods=['PUT'])
def edit_notebook():
    old_name = request.json.get('oldName')
    new_name = request.json.get('newName')
    notebooks = load_notebooks()
    
    if old_name in notebooks:
        index = notebooks.index(old_name)
        notebooks[index] = new_name
        save_notebooks(notebooks)
        return jsonify({"success": True, "notebooks": notebooks}), 200
    
    return jsonify({"success": False}), 400

@notes_blueprint.route('/notes/delete', methods=['DELETE'])
def delete_notebook():
    notebook_name = request.json.get('name')
    notebooks = load_notebooks()
    
    if notebook_name in notebooks:
        notebooks.remove(notebook_name)
        save_notebooks(notebooks)
        return jsonify({"success": True, "notebooks": notebooks}), 200
    
    return jsonify({"success": False}), 400
