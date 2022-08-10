# https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

from flask import Flask, request

app = Flask(__name__)

@app.route("/picking-numbers", methods=['PUT'])

def pickingNumbers():
    a = request.json["data"]
    maksimum = 0
    for item in set(a):
        objek1 = a.count(item)
        objek2 = a.count(item + 1)
        hitung = objek1 + objek2
        if hitung > maksimum:
            maksimum = hitung
    return {"result": maksimum}

# PUT /picking-numbers
# req body: { "data": [4,6,5,3,3,1] }
# resp body: { "result": 3 }