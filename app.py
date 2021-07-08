import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/moviedata'
app.config['SECRET_KEY'] = os.urandom(32)
migrate = Migrate(app, db)

db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)