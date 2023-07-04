from flask import Flask
import os
from flask_socketio import SocketIO
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

socketio = SocketIO(app)

if __name__ == '__main__':
    db.init_app(app)
    socketio.run(app, debug=True)
