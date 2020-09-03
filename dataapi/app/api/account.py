from . import api
from flask import jsonify, request
from ..models import Profile, Account
from .. import db

@api.route('/accounts', methods=['GET'])
def get_all_accounts():
    accounts = Account.query.all()
    object_json = {
        'accounts' : [account.to_json() for account in accounts],
        'status' : "OK"
    }

    return jsonify(object_json)

@api.route('/account', methods=['POST'])
def get_account():
    """
        example
        get account = {"id":1}
    """
    if(request.method == 'POST'):
        try:
            id_profile = request.json['id']
            print(id_profile)
            profile = Profile.query.filter_by(id=id_profile).first()
            if(profile != None):
                account = Account.query.filter_by(profile=profile).first()
                data_json = account.to_json()

                json_object = {
                    'account': data_json,
                    'status': 'OK'
                }

                return jsonify(json_object), 200
            else:
                json_object = {
                    'account': 'fail',
                    'status': 'OK'
                }

                return jsonify(json_object), 400

        except KeyError:
            json_object = {
                'authorization': 'fail',
                'status': 'key error'
            }
            return jsonify(json_object), 400
        except TypeError:
            json_object = {
                'authorization': 'fail',
                'status': 'type error'
            }
            return jsonify(json_object), 400
    else:
        json_object = {
            'account': 'fail',
            'status': 'bad request'
        }
        return jsonify(json_object), 400
        
@api.route('/account/transaction', methods=['PUT'])
def update_balance():
    """
        tipo de transação:
                            1: transferencia outro banco
                            2: pagamento
                            3: compra
                            4: deposito
                            5: transferencia mesmo banco

        example: {"AccountSource": "02.258-5", "value": 100, "type": 1, "AccountDest": "22.333-6"}
    """
    if request.method == 'PUT':
        try:
            account_source = request.json['AccountSource']
            value = request.json['value']
            type_transaction = request.json['type']
            account_dest = request.json['AccountDest']
            
            account_source_DB = Account.query.filter_by(account_number=account_source).first()
            account_dest_DB = Account.query.filter_by(account_number=account_dest).first()

            if(account_source_DB != None):
                if(type_transaction == 1 or type_transaction == 2 or type_transaction == 3):
                    if(value >= 0):
                        return validate_transaction_debit(account_source_DB, value)
                    else:
                        object_json = {
                            "transaction": "fail",
                            "reason" : "numero negativo",
                            "status": "OK"
                        }
                        return jsonify(object_json), 400
        
                elif(type_transaction == 4):    
                    if(value >= 0):
                        return validate_transaction_deposit(account_source_DB, value)
                    else:
                        object_json = {
                            "transaction": "fail",
                            "reason" : "numero negativo",
                            "status": "OK"
                        }
                        return jsonify(object_json), 400

                elif(type_transaction == 5):
                    if(value >= 0):
                        return validate_transation_tranfer(account_source_DB, account_dest_DB, value)
                    else:
                        object_json = {
                            "transaction": "fail",
                            "reason" : "numero negativo",
                            "status": "OK"
                        }
                        return jsonify(object_json), 400
                        
                else:
                    object_json = {
                            "transaction": "fail",
                            "reason" : "tipo de transação inválida",
                            "status": "OK"
                    }
                    return jsonify(object_json), 400
            else:
                object_json = {
                            "transaction": "fail",
                            "reason" : "Conta de origem não encontrada",
                            "status": "OK"
                }
                return jsonify(object_json), 400

        except KeyError:
            json_object = {
                'transaction': 'fail',
                'status': 'key error'
            }
            return jsonify(json_object), 400
        except TypeError:
            json_object = {
                'transaction': 'fail',
                'status': 'type error'
            }
            return jsonify(json_object), 400

    """ object_json = {
            "transaction": "success",
            "status": "OK"
    }
    return jsonify(object_json), 200 """


def validate_debit(balance, value):
    if(value > balance):
        return False
    else:
        return True

def validate_transaction_debit(account, value):
    
    balance = account.balance

    if (validate_debit(balance, value)):
        account.balance -= value
        db.session.add(account)
        db.session.commit()

        object_json = {
            "transaction": "success",
            "status": "OK"
        }
        return jsonify(object_json), 200
    else:
        object_json = {
            "transaction": "fail",
            "reason" : "Saldo insuficiente",
            "status": "OK"
        }
        return jsonify(object_json), 200

def validate_transaction_deposit(account, value):
    account.balance += value
    db.session.add(account)
    db.session.commit()

def validate_transation_tranfer(account_source, account_dest, value):

    if(account_source.account_number == account_dest.account_number):
        object_json = {
            "transaction": "fail",
            "reason" : "conta de origem é igual a de destino",
            "status": "OK"
        }
        return jsonify(object_json), 400
    else:
        
        if(account_dest != None):
            balance_account_source = account_source.balance
            
            if(validate_debit(balance_account_source, value)):
                account_source.balance -= value
                account_dest.balance += value

                db.session.add(account_source)
                db.session.add(account_dest)
                db.session.commit()

                object_json = {
                    "transaction": "success",
                    "status": "OK"
                }
                return jsonify(object_json), 200
            else:
                object_json = {
                    "transaction": "fail",
                    "reason" : "saldo insuficiênte",
                    "status": "OK"
                }
                return jsonify(object_json), 400
        else:
            object_json = {
                "transaction": "fail",
                "reason" : "conta de destino não existe",
                "status": "OK"
            }
            return jsonify(object_json), 400
                        
                    
