import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account.
cred = credentials.Certificate('credentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

users_ref = db.collection('users')
meals_ref = db.collection('meals')
users_docs = users_ref.stream()
meals_docs = meals_ref.stream()
