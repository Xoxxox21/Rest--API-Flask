from flask import Flask, jsonify, request,make_response
from flask_restful import Api


app = Flask(__name__)

api = Api(app)

identitas = {}
@app.route('/service/<string:name>', methods=['POST'])
def service(name):
    if request.is_json:
        
        req = request.get_json()
        
        response = {
            "status" : 200,
            "message_status" : "Success",
            'data' : [req]
        }
        res = make_response(jsonify(response), 200)
        return  res
    else:
        res = make_response(jsonify({"message" : "No JSON received"}), 400)
        return  res
        
if __name__ == "__main__":
    app.run(debug=True, port=5000)