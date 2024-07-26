from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,Categories
from flask_cors import CORS

category_blueprint=Blueprint('categories',__name__,url_prefix='/category')
