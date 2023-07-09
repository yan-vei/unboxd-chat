from flask import Flask
import os
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

socketio = SocketIO(app, manage_session=False)

if __name__ == '__main__':
    app.run(debug=True)
