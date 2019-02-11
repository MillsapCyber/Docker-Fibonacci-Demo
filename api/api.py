import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
class Product(Resource):
    def get(self):
        x,y=0,1
        var = [];
        while y <= 60:
            var.append(y)
            x,y=y,x+y
        return var
api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
