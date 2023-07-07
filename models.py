from mongoengine import Document, StringField, IntField

class User(Document):
    name = StringField(max_length=200)
    age = IntField()
    mobile = StringField()
    