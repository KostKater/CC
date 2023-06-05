from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account.
cred = credentials.Certificate('credentials.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection('users')
docs = users_ref.stream()

# print(docs)
for doc in docs:
    print(doc.to_dict())
    # print(f'{doc.id} => {doc.to_dict()}')

app = FastAPI()


@app.get("/")
def index():
    return {"hello": "FastAPI"}
