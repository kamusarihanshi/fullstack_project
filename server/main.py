from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app=app, db=db)



@app.route('/', methods=['GET'])
def movies():
    response_dict = {
        "text": "Movies will go here"
    }

    return make_response(jsonify(response_dict), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5555)