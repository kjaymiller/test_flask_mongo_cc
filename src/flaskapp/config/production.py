import os

import pymongo

# Create a mongoDB Connection
client = pymongo.MongoClient("DATABASE_CONNECTION_STRING")
DEBUG = False

if "WEBSITE_HOSTNAME" in os.environ:
    ALLOWED_HOSTS = [os.environ["WEBSITE_HOSTNAME"]]
else:
    ALLOWED_HOSTS = []


dbuser = os.environ["MONGO_USERNAME"]
dbpass = os.environ["MONGO_PASSWORD"]
dbhost = os.environ["MONGO_HOST"]
dbname = os.environ["MONGO_DATABASE"]
DATABASE_URI = f"mongodb://{dbuser}:{dbpass}@{dbhost}/{dbname}?authSource=admin"
