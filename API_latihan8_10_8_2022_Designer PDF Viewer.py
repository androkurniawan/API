# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?h_r=next-challenge&h_v=zen&isFullScreen=false

from flask import Flask, request

app = Flask(__name__)
@app.route("/pdf-viewer")

def designerPdfViewer():
    word = request.args.get("word")
    h = request.json["height"]
    huruf = ["a","b","c","d","e",'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    kamus = {}
    elemen = []
    for i in range(len(huruf)):
        for j in range(len(h)):
            if i == j:
                kamus[huruf[i]] = h[j]
    for item in word:
        elemen.append(kamus.get(item))
    return {
        "area" : (max(elemen)*len(elemen))}

# GET /pdf-viewer?word=torn 
# Req body: { "height": [1,2,3,3,2,...] } 
# Resp body: { "area": "9 mm2" }