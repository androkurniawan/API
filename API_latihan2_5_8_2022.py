from flask import Flask, request

app = Flask(__name__)

@app.route('/hello-json', methods=['GET'])
def hello():
    a = request.args.get('name')
    return {
        "message" : "Hello " + a
    }

# Latihan 2 
# GET /hello-json?name=andri  
# Response: { "message": "Hello Andri!" }
# Response header: Content-Type: application/json 