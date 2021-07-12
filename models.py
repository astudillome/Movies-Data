from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.Date)
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    actors = db.relationship('Actor', backref='movie', lazy=True)

    @property
    def search_title(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    def __repr__(self):
        return '<Movie {}'.format(self.name)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
class Actor(db.Model):
    __tablename__ = 'actors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    movies = db.relationship('Movie', backref='actor', lazy=True)
    
    @property
    def search_term(self):
        return {
            'id': self.id,
            'name': self.name,
            'movies': self.movies
        }
        
    def __repr__(self):
        return '<Actor {}'.format(self.name)
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
db.create_all()
