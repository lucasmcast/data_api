from flask import Blueprint

api = Blueprint('api', __name__)

from . import profile, authentication, errors, account