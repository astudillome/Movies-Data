import os
from flask import Flask
from flask_migrate import Migrate
from models import *
from flask_cors import CORS



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/moviedata'
app.config['SECRET_KEY'] = os.urandom(32)
migrate = Migrate(app, db)
CORS(app)
db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)