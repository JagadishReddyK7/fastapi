from fastapi import FastAPI
from pymongo import MongoClient
import json


app=FastAPI()

dbcon=MongoClient("mongodb+srv://kollujagadishreddy:jagadish17@cluster0.gtfxrem.mongodb.net/")
db=dbcon.get_database("fastapi")
collection=db.user

@app.get("/")
def home():
    return {"message":"Hello World"}

@app.get("/get_users")
def get_users():
    users=list(collection.find())
    for user in users:   
        del user["_id"]
    print(users)
    return users

@app.post("/insert_user")
def insert_user(document: dict):
    collection.insert_one(document)
    return {"message":"Data inserted succesfully!"}