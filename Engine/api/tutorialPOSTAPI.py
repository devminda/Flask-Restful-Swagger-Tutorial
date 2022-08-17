from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse
from api.app import api
class postingDetails(Resource):
    def post(self):
        """
        post end point
        ---
        tags:
            - Post user details 
        security:
            - APIKeyHeader: ['Authorization']
        consumes:
            - application/json
        parameters:
            - in: body
              name: details
              schema:
              id: details
              required:
                - Name
                - Country
                - Age
              properties:
                    Name:
                      type: string
                      description: Name
                    Country:
                      type: string
                      description: Country of origin
                      default: USA
                    Age: 
                      type: integer
                      description: Age of the person
        responses:
            200:
                description: The article is
            400:
                description: wrong type of data     
        """
        parser = reqparse.RequestParser()
        parser.add_argument('Name', type=str)
        parser.add_argument('Country', type=str)
        parser.add_argument('Age', type=int)

        args = parser.parse_args()
        name = args['Name']
        country = args['Country']
        age = args['Age']
        result = {
            "Name of Person": name,
            "Country of Origin": country,
            "Age of person" : age
        }
        status = True
        resp = make_response(jsonify({"results":result, "status":status}))
        return resp

class postingFile(Resource):
    def post(self):
        """
        post end point
        ---
        tags:
            - Post a file
        security:
            - APIKeyHeader: ['Authorization']
        consumes:
            - multipart/form-data
        parameters:
            - in: formData
              name: upfile
              type: file
              description: The file to upload.
                
        responses:
            200:
                description: The article is
                
            400:
                description: wrong type of data
        """
        file = request.files['upfile']
        result = file.filename
        status = True
        resp = make_response(jsonify({"results":result, "status":status}))
        return resp

api.add_resource(postingDetails,'/postingDetails')
api.add_resource(postingFile,'/postingFile')