from fastapi import FastAPI
from pymongo import MongoClient
import json


app=FastAPI()

dbcon=MongoClient("mongodb+srv://kollujagadishreddy:jagadish17@cluster0.gtfxrem.mongodb.net/")
db=dbcon.get_database("fastapi")
records=db.user

@app.get("/")
def home():
    return {"message":"Hello World"}

@app.get("/get_user")
def get_users():
    users=records.find().to_json()
    user=json.loads(users)
    print(user)
    return {"users":user}

@app.post("/insert_user")
def insert_user(document: dict):
    records.insert_one(document)
    return {"message":"Data inserted succesfully!"}