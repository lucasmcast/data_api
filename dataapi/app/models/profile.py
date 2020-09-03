from . import db

class Profile(db.Model):

    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(40))
    password = db.Column(db.String(20))
    url_foto = db.Column(db.String(400))
    account = db.relationship('Account', backref='profile', lazy='dynamic')
    
    def __repr__(self):
        return f'<Profile id={self.id}, email={self.email}, nome={self.name},\
            senha={self.password}, url_foto={self.url_foto}>'

    def to_json(self):
        json_generate = {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'url_foto': self.url_foto,
        }

        return json_generate