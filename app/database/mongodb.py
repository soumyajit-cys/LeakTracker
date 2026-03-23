import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

breach_collection = db["breach_data"]
keyword_collection = db["keywords"]
alert_collection = db["alerts"]

# Indexing
keyword_collection.create_index("value", unique=True)
breach_collection.create_index("email")
alert_collection.create_index("keyword")