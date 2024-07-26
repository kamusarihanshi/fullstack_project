from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,Payment
from flask_cors import CORS
payment_bp=Blueprint('payment',__name__,url_prefix='/payment')
payment_api=Api(payment_bp)
CORS(payment_bp)