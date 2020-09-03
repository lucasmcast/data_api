from . import api
from flask import jsonify, request
from ..models import Profile, Account
from .. import db
import random
from sqlalchemy.exc import IntegrityError 

@api.route('/profiles', methods=['GET'])
def profiles():
    profiles = Profile.query.all()
    list_json = [profile.to_json() for profile in profiles]
    json_object = {
        'profiles': list_json,
        'status': 'OK'
    }
    return jsonify(json_object), 200

@api.route('/createProfile', methods=['POST'])
def create_profile():
    if(request.method == 'POST'):
        try:
            email = request.json['email']
            name = request.json['name']
            password = request.json['password']
            url_foto = request.json['urlFoto']
            number_register = request.json['numberRegister']

            profile = Profile(email=email, name=name, password=password, url_foto=url_foto)
            prefix_account = random.randint(100, 999)
            number_account = f'25.{str(prefix_account)}-5'
            
            account = Account(full_name=name, balance=0, account_number=number_account, number_register=number_register)

            db.session.add_all([profile, account])
            db.session.commit()
            
            return jsonify({'createProfile': 'success', 'status': 'ok'})

        except KeyError:
            json_object = {
                'createProfile': 'fail',
                'status': 'key error'
            }
            return jsonify(json_object), 400
        except TypeError:
            json_object = {
                'createProfile': 'fail',
                'status': 'type error'
            }
            return jsonify(json_object), 400
        except IntegrityError:
            json_object = {
                'reason': 'email, numberRegister ou accountNumber ja foram cadastrados',
                'createProfile': 'fail',
                'status': 'IntegrityError'
            }
            return jsonify(json_object), 400