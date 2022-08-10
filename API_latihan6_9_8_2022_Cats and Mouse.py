# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

from flask import Flask, request

app = Flask(__name__)
@app.route("/cat-and-mouse/x/<input_x>")

def catAndMouse(input_x):
    x = int(input_x)
    y = int(request.args.get("y"))
    z = int(request.headers.get("z"))
    if abs(x-z) < abs(y-z):
        return {"message" : "Cat A"}
    if abs(x-z) > abs(y-z):
        return {"message" : "Cat B"}
    else:
        return {"message" : "Mouse C"}

# GET /cat-and-mouse/x/1?y=2
# req header: z=3
# resp body: { "message": "Cat B" }