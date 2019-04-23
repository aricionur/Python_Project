from pymongo import MongoClient
from entity import Car

print("pymongo_module started...\n")

client = MongoClient()

db = client.test_db

collection = db.test_collection

collection.drop()

def insert_single_doc(doc):
    object_id = collection.insert_one(doc).inserted_id
    return object_id

def insert_many_docs(docs):
    result = collection.insert_many(docs)
    return result

def get_first_doc():
    return collection.find_one()

def get_single_doc(key, value):                  #returns first matching doc in collection
    return collection.find_one({key: value})

def get_doc_by_objectId(object_id):
    return collection.find_one(object_id)

def get_all_collection():
    cursor = collection.find()
    return [Car(next["name"], next["price"]) for next in cursor]


cars = [{'name': 'Audi', 'price': 200},
        {'name': 'Mercedes', 'price': 57127},
        {'name': 'Skoda', 'price': 9000},
        {'name': 'Volvo', 'price': 29000},
        {'name': 'Bentley', 'price': 350000},
        {'name': 'Citroen', 'price': 21000},
        {'name': 'Hummer', 'price': 41400},
        {'name': 'Volkswagen', 'price': 21600}]

audi_2 = {'name': 'Audi', 'price': 100}
insert_single_doc(audi_2)

insert_many_docs(cars)


print("First doc is : \n", get_first_doc())

print("Price of Audi is : \n", get_single_doc("name", "Audi"))


audi_3 = {'name': 'Audi', 'price': 5500}
object_id = insert_single_doc(audi_3)
print("doc with object_id :", object_id, "is :", get_doc_by_objectId(object_id) )


print("printing test_collection :")
car_list = get_all_collection()
for car in car_list:
    print(car.name, ":", car.price)


print("\nprogram ended...")