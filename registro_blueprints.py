from routes.home_page.home_page import home_page_blueprint
from routes.colleges.colleges import colleges_blueprint
from routes.courses.courses import courses_blueprint
from routes.notifications.notifications import notifications_blueprint
from routes.notes.notes import notes_blueprint
from routes.calendar.calendar import calendar_blueprint
from routes.configuracoes.configuracoes import configuracoes_blueprint

def registro_blueprints(app):
    app.register_blueprint(home_page_blueprint)
    app.register_blueprint(colleges_blueprint)
    app.register_blueprint(courses_blueprint)
    app.register_blueprint(notifications_blueprint)
    app.register_blueprint(notes_blueprint)
    app.register_blueprint(calendar_blueprint)
    app.register_blueprint(configuracoes_blueprint)