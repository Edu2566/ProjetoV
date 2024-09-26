from flask import Blueprint, render_template, url_for
from api.CollegeAPI import CollegeAPI

college_api_instance = CollegeAPI()
colleges_blueprint = Blueprint('colleges', __name__, template_folder='templates', static_folder='static-colleges')

@colleges_blueprint.route('/colleges-information/<int:college_id>')
def college_information(college_id):
    college_data = college_api_instance.get_college_by_id(college_id)
    
    if 'error' in college_data:
        return college_data['error'], 404
    
    return render_template('colleges-information.html', college=college_data)

@colleges_blueprint.route('/view-exam/<int:exam_id>')
def view_exam(exam_id):
    exam_data = college_api_instance.get_exam_by_id(exam_id)
    
    if 'error' in exam_data:
        return exam_data['error'], 404
    
    pdf_url = exam_data["exam_pdf_url"]
    college_data = college_api_instance.get_college_by_id(exam_data['college_id'])
    template_data = next((item for item in college_data['template'] if item['exam_id'] == exam_id), None)
    template_url = template_data['template_pdf_url'] if template_data else "#"

    return render_template('view-exam.html', pdf_url=pdf_url, template_url=template_url)
