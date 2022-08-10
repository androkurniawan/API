from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    nama = request.args.get('name')
    return f"Hello {nama}"



# Latihan 1
# GET /hello?name=foo 
# Response: "Hello Foo!" 