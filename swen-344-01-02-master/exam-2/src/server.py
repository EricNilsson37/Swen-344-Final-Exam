from flask import Flask
from flask_restful import Resource, Api
from api.exam_endpoints import ExampleEndpoint, User, UserBleats, CreateBleat, Edit, Delete, GetInfo

app = Flask(__name__)
api = Api(app)

api.add_resource(ExampleEndpoint, '/')
api.add_resource(User, '/users/<string:username>')
api.add_resource(UserBleats, '/users/<string:name>/bleats')
api.add_resource(CreateBleat, '/compose/bleat')
api.add_resource(Edit, '/edit/bleat')
api.add_resource(Delete, '/delete/bleat')
api.add_resource(GetInfo, '/info/<int:ID>')

if __name__ == '__main__':
    app.run(debug=True)
