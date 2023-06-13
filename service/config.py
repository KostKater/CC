import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
from os import environ as env
import requests


config = {
    "apiKey": "AIzaSyBnCn5IwBNqqkFWma-eiS2DFJOm34K7-w0",
    "authDomain": "kost-kater.firebaseapp.com",
    "projectId": "kost-kater",
    "databaseURL": "",
    "storageBucket": "kost-kater.appspot.com",
    "messagingSenderId": "962954133251",
    "appId": "1:962954133251:web:e8c90794444104b7203336",
    "measurementId": "G-B01WLF1L6D"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()

url = env['FIREBASE_CRED']
local_filepath = "credential.json"
response = requests.get(url)
with open(local_filepath, "wb") as file:
    file.write(response.content)

cred = credentials.Certificate("credential.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()
