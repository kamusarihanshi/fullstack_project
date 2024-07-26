from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,Products
from flask_cors import CORS
product_bp=Blueprint('product',__name__,url_prefix='/product')
product_api=Api(product_bp)

CORS(product_bp)