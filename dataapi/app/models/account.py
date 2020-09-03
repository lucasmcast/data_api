from . import db

class Account(db.Model):

    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    balance = db.Column(db.Float)
    account_number = db.Column(db.String(10), unique=True)
    number_register = db.Column(db.String(20), unique=True)
    id_profile = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    # extracts = db.relationship('Extract', backref='account', lazy='dynamic')
    # last_transaction = db.relationship('LastTransaction', backref='account', lazy='dynamic')

    def __repr__(self):
        return f'<Account id={self.id}, full_name={self.full_name}, balance={self.balance},\
            account_number={self.account_number}, number_register={self.number_register} id_profile={self.id_profile}>'

    def to_json(self):
        json_generate = {
            'id': self.id,
            'full_name': self.full_name,
            'balance': self.balance,
            'account_number': self.account_number,
            'number_register': self.number_register
        }

        return json_generate
