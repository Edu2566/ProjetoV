from flask import Flask
from registro_blueprints import registro_blueprints

app = Flask(__name__, static_folder='static', static_url_path='/static')

registro_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)