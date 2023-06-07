import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

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
# db = firebase.database()
# db = firestore.Client(project="kost-kater")
cred = credentials.Certificate('credentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
