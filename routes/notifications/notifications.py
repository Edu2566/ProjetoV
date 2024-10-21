from flask import Blueprint, render_template

notifications_blueprint = Blueprint('notifications', __name__, template_folder='templates', static_folder='static-notifications')

@notifications_blueprint.route('/notifications')
def notifications_menu():
    return render_template('notifications-menu.html')