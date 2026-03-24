from app.database.mongodb import breach_collection

def save_breach_data(data):
    if data:
        breach_collection.insert_many(data)

def get_breach_data():
    return list(breach_collection.find({}, {"_id": 0}))


