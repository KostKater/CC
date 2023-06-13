from service.config import db


def read_users_collection():
    users_ref = db.collection("users")
    docs = users_ref.stream()
    users_list = []

    for doc in docs:
        user_data = doc.to_dict()
        users_list.append(user_data)

    return users_list


def read_user_doc(email):
    doc_ref = db.collection("users").document(email)
    doc = doc_ref.get()
    return doc.to_dict()


def add_user_doc(email):
    data = {
        "email": email,
        "eat_halal": True,
        "allergies": []
    }

    db.collection("users").document(email).set(data)


def update_user_doc(email, eat_halal, allergies):
    data = {
        "email": email,
        "eat_halal": eat_halal,
        "allergies": allergies
    }

    db.collection("users").document(email).set(data)
