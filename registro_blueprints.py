from routes.homePage.homePage import homePage_blueprint
from routes.faculdades.faculdades import faculdades_blueprint
from routes.cursos.cursos import cursos_blueprint
from routes.notificacoes.notificacoes import notificacoes_blueprint
from routes.anotacoes.anotacoes import anotacoes_blueprint
from routes.calendario.calendario import calendario_blueprint
from routes.configuracoes.configuracoes import configuracoes_blueprint
from routes.provas.provas import provas_blueprint

def registro_blueprints(app):
    app.register_blueprint(homePage_blueprint)
    app.register_blueprint(faculdades_blueprint)
    app.register_blueprint(cursos_blueprint)
    app.register_blueprint(notificacoes_blueprint)
    app.register_blueprint(anotacoes_blueprint)
    app.register_blueprint(calendario_blueprint)
    app.register_blueprint(configuracoes_blueprint)
    app.register_blueprint(provas_blueprint)
