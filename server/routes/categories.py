from flask import Blueprint
from flask_restful import Api,Resource,reqparse
from models import db,Categories
from flask_cors import CORS


category_bp=Blueprint('category',__name__,url_prefix='/category')
category_api=Api(category_bp)
CORS(category_bp)

category_parser=reqparse.RequestParser()
category_parser.add_argument('name',type=str,required=True,help='Name is required')
category_parser.add_argument('description',type=str,required=False,help='not required')

class Category(Resource):
    def get(self,id):
        category=Categories.query.get(id)
        return {'id':category.id, 'name':category.name, 'description':category.description}
    def post(self):
        data=category_parser.parse_args()
        new_category=Categories(name=data['name'], description=data['description'])
        db.session.add(new_category)
        db.session.commit()
        return {'message':'Category added successfully'},201
    def put(self,id):
        data=category_parser.parse_args()
        category=Categories.query.get(id)
        category.name=data['name']
        category.description=data['description']
        db.session.commit()
        return {'message':'Category updated successfully'},200
    def delete(self,id):
        category=Categories.query.get(id)
        db.session.delete(category)
        db.session.commit()
        return {'message':'Category deleted successfully'},200
        
        