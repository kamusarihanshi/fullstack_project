from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,Orders
from flask_cors import CORS

order_bp=Blueprint('order',__name__,url_prefix='/order')
order_api=Api(order_bp)
CORS(order_bp)
