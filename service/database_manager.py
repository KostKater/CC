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
        "allergies": [],
        "ingredients": [],
        "price_min": 0,
        "price_max": 999999999
    }

    db.collection("users").document(email).set(data)


def update_user_doc(email, eat_halal, allergies, ingredients, price_min, price_max):
    doc_ref = db.collection("users").document(email)
    if eat_halal != True:
        doc_ref.update({"eat_halal": eat_halal})
    if allergies != []:
        doc_ref.update({"allergies": allergies})
    if ingredients != []:
        doc_ref.update({"ingredients": ingredients})
    if price_min != 0:
        doc_ref.update({"price_min": price_min})
    if price_max != 999999999:
        doc_ref.update({"price_max": price_max})
