from flask_restful import Resource, reqparse
from db.swen344_db_utils import connect, exec_sql_file, exec_get_all, exec_commit, exec_get_one
from flask import request

class ExampleEndpoint(Resource):
    def get(self):
        return exec_get_all('SELECT * FROM BLEATS')

class User(Resource):
    def get(self, username):
        return exec_get_all('SELECT * FROM USERS WHERE USER_NAME = %s', [username])

class UserBleats(Resource):
    def get(self, name):
        user_id = exec_get_one('SELECT ID FROM USERS WHERE USER_NAME = %s', [name])

        return exec_get_all('SELECT * FROM BLEATS WHERE USER_ID = %s', [user_id])

parser = reqparse.RequestParser()
parser.add_argument('ID', type = int )
parser.add_argument('USER_ID', type = int)
parser.add_argument('BLEAT_CONTENT', type = str)

class CreateBleat(Resource):
    def post(self):

        args = parser.parse_args()

        exec_commit('INSERT INTO BLEATS (ID, USER_ID, BLEAT_CONTENT) VALUES(%s,%s,%s)', [args['ID'], args['USER_ID'], args['BLEAT_CONTENT']])


class Edit(Resource):
    def put(self):

        args = parser.parse_args()
        
        return exec_commit('UPDATE BLEATS SET ID = %s, USER_ID = %s, BLEAT_CONTENT= %s WHERE ID = %s', [args['ID'], args['USER_ID'], args['BLEAT_CONTENT'], args['ID']])

class Delete(Resource):
    def delete(self):

        args = request.args

        return exec_commit('DELETE FROM BLEATS WHERE ID = %s', args['ID'])

class GetInfo(Resource):
    def get(self, ID):
        value = exec_get_all('SELECT * FROM BLEATS WHERE ID = %s', [ID])

        return value[0][2]