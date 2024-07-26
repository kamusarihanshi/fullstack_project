from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,Reviews
from flask_cors import CORS


reviews_bp=Blueprint('reviews',__name__,url_prefix='/reviews')
reviews_api=Api(reviews_bp)
CORS(reviews_bp)