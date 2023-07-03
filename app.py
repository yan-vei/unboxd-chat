from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_socketio import SocketIO

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)
socketio = SocketIO(app)


if __name__ == '__main__':
    db.init_app(app)
    socketio.run(app, debug=True)
