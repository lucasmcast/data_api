from . import db

class LastTransaction(db.Model):

    __tablename__ = 'last_transactions'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    destination = db.Column(db.String(100))
    value = db.Column(db.Integer)
    # account_id = db.relationship(db.Integer, db.ForeignKey('accounts.id'))

    def __repr__(self):
        return f'<LastTransaction id={self.id}, status={self.status}, destination={self.destination},\
            value={self.value}>'

    def to_json(self):
        json_generate = {
            'id': self.id,
            'status': self.status,
            'destination': self.destination,
            'value': self.value,
        }

        return json_generate