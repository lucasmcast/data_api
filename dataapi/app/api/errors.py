from . import api
from flask import jsonify
from ..models import Profile, Account

@api.app_errorhandler(404)
def page_not_found(e):
    response = jsonify({'status': '404 not found'})
    return response, 404
   
@api.app_errorhandler(405)
def method_not_allowed(e):
    response = jsonify({'status': 'method not allowed'})
    return response, 405

@api.app_errorhandler(400)
def bad_request(e):
    response = jsonify({'status': 'bad request'})
    return response, 400