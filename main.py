from flask import Flask
from routes.home import homeRoute

app = Flask(__name__)

app.register_blueprint(homeRoute)

app.run(debug=True)