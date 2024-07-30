from flask import Blueprint, render_template, send_file

provas_blueprint = Blueprint('provas', __name__, static_folder='static-provas', template_folder='templates')

@provas_blueprint.route('/provas')
def provas_menu():
    return render_template('provasMenu.html')

@provas_blueprint.route('/exams-information')
def exams_information():
    return render_template('exams-information.html')

@provas_blueprint.route('/view-exam')
def view_exam():
    return render_template('view-exam.html')

@provas_blueprint.route('/pdf')
def pdf():
    return send_file('./pdf/Prova.pdf')