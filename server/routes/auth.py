from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,User
from flask_cors import CORS
from flask_bcrypt import Bcrypt


auth_bp=Blueprint('user',__name__,url_prefix='/user')
auth_api=Api(auth_bp)
CORS(auth_bp)
bcrypt=Bcrypt()








