from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from api.app import api

class Helloworld(Resource):
    def get(self):
        """
        get end point
        ---
        tags:
            - Tutorial
        security:
            - APIKeyHeader: ['Authorization']
        consumes:
            - application/json
        # parameters:
        #     - in: path
        #       name: name
        #       type: string
        #       description: The file to string.
                
        responses:
            200:
                description: The article is
                
            400:
                description: wrong type of data
        """
        status = True
        resp = make_response(jsonify({"results":"heeloworld", "status":status}))
        return resp

class postingName(Resource):
    def post(self):
        """
        post end point
        ---
        tags:
            - Post Tutorial
        security:
            - APIKeyHeader: ['Authorization']
        consumes:
            - multipart/form-data
        parameters:
            - in: body
              name: data
              type: file
              description: The file to upload.
                
        responses:
            200:
                description: The article is
                
            400:
                description: wrong type of data
        """
api.add_resource(Helloworld,'/Helloworld')