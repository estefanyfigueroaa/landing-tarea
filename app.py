from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Landing.db import landingdb
from routes.msg import msg

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

# register blueprints

app.register_blueprint(msg)