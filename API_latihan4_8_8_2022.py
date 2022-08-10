import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/car-manufacturer', methods=['POST'])
def kendaraan():
    a = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json')
    x = a.json()
    country = request.get_json()
    pabrik = []
    for item in x["Results"]:
        if item["Country"] == country["Country"]:
            pabrik.append(item["Mfr_Name"])
    return {
        "Manufacturer" : pabrik
    } 

# Latihan 4 
# POST /car-manufacturer 
# Request body: { "country": "UK" }
# Response: { "manufacturers": [] }