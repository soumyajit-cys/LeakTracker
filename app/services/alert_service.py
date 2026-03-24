from app.database.mongodb import alert_collection

def create_alert(keyword, data):
    alert = {
        "keyword": keyword,
        "matched_data": data
    }
    alert_collection.insert_one(alert)

def get_alerts():
    return list(alert_collection.find({}, {"_id": 0}))