# https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=false

from flask import Flask, request

app = Flask(__name__)
@app.route("/hurdle-race/k/<input_k>")

def hurdleRace(input_k):
    k = int(input_k)
    tinggi = request.json["height"]
    if k < max(tinggi):
        return {"min_doses" : (max(tinggi) - k)}
    else:
        return {"min_doses" : 0}

# GET /hurdle-race/k/1
# Req body: { "height": [1,2,3,3,2] } 
# Resp body: { "min_doses": 2 }