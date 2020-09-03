from . import db

class Extract(db.Model):

    __tablename__ = 'extracts'
    id = db.Column(db.Integer, primary_key=True)
    status_purchase = db.Column(db.Integer)
    destination = db.Column(db.String(100))
    value = db.Column(db.Integer)
    date = db.Column(db.String(20))
    # account_number = db.relationship(db.String(10), db.ForeignKey('accounts.account_number'))
    
    def __repr__(self):
        return f'<Extract id={self.id}, status_purchase={self.status_purchase}, destination={self.destination},\
            value={self.value}, date={self.date}>'

    def to_json(self):
        json_generate = {
            'id': self.id,
            'status_purchase': self.status_purchase,
            'destination': self.destination,
            'value': self.value,
            'date': self.date,
        }

        return json_generate