from . import api
from flask import jsonify, request
from ..models import Profile, Account


@api.route('/authentication', methods=['POST'])
def auth():
    data_json = {}
    if(request.method == 'POST'):
        try:

            login = request.json['login']
            password = request.json['password']

            profile = Profile.query.filter_by(email=login).first()
            print(login)
            if(profile != None):
                if(profile.password == password):
                    data_json = profile.to_json()
                else:
                    data_json = 'fail'
            else:
                data_json = 'fail'
            
            json_object = {
                'authorization': data_json,
                'status': 'OK'
            }

            return jsonify(json_object), 200
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
            'authorization': 'fail',
            'status': 'bad request'
        }
        return jsonify(json_object), 400
