from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from api.app import api

class Helloworld_v1(Resource):
    def get(self):
        """
        get end point
        ---
        tags:
            - Get with parameters
        security:
            - APIKeyHeader: ['Authorization']
        consumes:
            - application/json
        parameters:
            - in: query
              name: value
              type: string
              description: Value to execute
                
        responses:
            200:
                description: The article is
                
            400:
                description: wrong type of data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('value')


        args = parser.parse_args()
        if args['value'] == 'hello':
            result = "hello world"
        else:
            result = "good morning world"

        status = True
        resp = make_response(jsonify({"results":result, "status":status}))
        return resp

class Helloworld_v2(Resource):
    def get(self):
        """
        get end point
        ---
        tags:
            - Get without parameters
        security:
            - APIKeyHeader: ['Authorization']
        consumes:
            - application/json
        responses:
            200:
                description: The article is
                
            400:
                description: wrong type of data
        """
        
        status = True
        resp = make_response(jsonify({"results":"Hey there", "status":status}))
        return resp

api.add_resource(Helloworld_v1,'/Helloworld_v1')
api.add_resource(Helloworld_v2,'/Helloworld_v2')
