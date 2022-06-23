from codecs import namereplace_errors
from crypt import methods
from urllib import response
from flask import Flask, Request, request
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS(app)

identitas = {}

class ContohResource(Resource):
    def get(self):
        # response = {'msg':'hello'}
        
        return identitas
        
    def post(self):
        name = request.form['name']
        umur = request.form['umur']
        identitas['name'] = name
        identitas['umur'] = umur
        response = {'msg': 'Data Berhasil Dimasukkan'}
        return response
        
        
api.add_resource(ContohResource, '/api', methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True, port=5000)