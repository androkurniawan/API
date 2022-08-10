import requests, base64
from flask import Flask, request

app = Flask(__name__)
def basicAuth():
    pass_str = request.headers.get("Authorization")
    pass_tanpa_basic = pass_str.replace("Basic ","")
    hasil_decode = base64.b64decode(pass_tanpa_basic)                   #********************************************
    hasil_decode_tanpa_b = hasil_decode.decode("utf-8")                 #*******************************************
    username_aja = hasil_decode_tanpa_b.split(":")[0]
    password_aja = hasil_decode_tanpa_b.split(":")[1]
    if username_aja == "andro" and password_aja == "password1":
        return True

@app.route('/weather')
def latihan3():
    if basicAuth():    
        a = request.headers.get('city')
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={a}&appid=0af7650b00321f8081a8a9ad3a838f51')
        b = r.json()    
        return {
            'Weather' : b['weather'][0]['main'],
            'Coord' : b['coord'],
            'Temp' : b['main']['temp']
                },200
    else:
        return{
            '401' : "Salah satu username atau password salah"
        },401

# Latihan 3
# GET /weather 
# request header: city=bandung 
# Response: {"weather":"Cloudy","coordinate":{"lat":1,"lon":2},"temperature":1}