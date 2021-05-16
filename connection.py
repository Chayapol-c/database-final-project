"""
Connect MongoDB and 
"""
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://chayapol:cde8ac39@cluster0.vz75m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["BobaMilkTeaShop"]
beverages = db["beverages"]
bills = db["bills"]
discounts = db["discounts"]
customers = db["customers"]
equipments = db["equipments"]
