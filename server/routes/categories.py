from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,Categories
from flask_cors import CORS


category_bp=Blueprint('category',__name__,url_prefix='/category')
category_api=Api(category_bp)
CORS(category_bp)
