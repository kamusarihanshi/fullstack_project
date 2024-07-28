from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,User
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


auth_bp=Blueprint('user',__name__,url_prefix='/user')
auth_api=Api(auth_bp)
CORS(auth_bp)
bcrypt=Bcrypt()
jwt=JWTManager()

Register_parser=reqparse.RequestParser()
Register_parser.add_argument('username',type=str,required=True,help='Username is required')
Register_parser.add_argument('email',type=str,required=True,help='Email is required')
Register_parser.add_argument('password',type=str,required=True,help='Password is required')


class Register(Resource):
    def post(self):
        data=Register_parser.parse_args()
        hashed_password=bcrypt.generate_password_hash(data['password'])
        new_user=User(username=data['username'],email=data['email'],password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {'message':'User registered successfully'},201




