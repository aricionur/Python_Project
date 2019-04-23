from pymongo import MongoClient
from entity import Car

print("pymongo_module started...\n")

client = MongoClient()

db = client.test_db

collection = db.test_collection

####### Insert a document
# post = { "author": "onur_3",
#          "text": "my first blog post"
#          }
# result = collection.insert_one(post)
# print("resulted id :", result.inserted_id)

##### Insert many docs

cars = [ {'name': 'Audi', 'price': 52642},
         {'name': 'Mercedes', 'price': 57127},
         {'name': 'Skoda', 'price': 9000},
         {'name': 'Volvo', 'price': 29000},
         {'name': 'Bentley', 'price': 350000},
         {'name': 'Citroen', 'price': 21000},
         {'name': 'Hummer', 'price': 41400},
         {'name': 'Volkswagen', 'price': 21600} ]

collection.insert_many(cars)

cursor = collection.find()

# ref_car = Car("audi", "150")
# print(ref_car)



print("all collection and add to car_list :")
car_list = [Car(next["name"], next["price"]) for next in cursor]
# car_list = []
# for next in cursor:
#
#     # print(next["name"], ":", next["price"])
#     car_list.append( Car( next["name"], next["price"] ) )

print("printing car list :")
for car in car_list:
    print(car.name, car.price)


# all_collection = [next for next in cursor]
#
# for next in all_collection:
#     print(next["name"])

collection.drop()


# print("next doc : ", cursor.next())
# print("next doc : ", cursor.next())
# print("next doc : ", cursor.next())
# print("next doc : ", cursor.next())


####### Get a first document ****
# result = collection.find_one()
#
# print("result :", result[_id])

###### Get a single document ****
# result = collection.find_one({"author": "onur_3"})
# print("result :", result)

###### Query bu ObjectId
# post = {"author": "onur_6",
#         "text": "inserting onur_6"}
# object_id = collection.insert_one(post).inserted_id
#
# print("gettting doc by object_id")
# returned_doc = collection.find_one({"_id": object_id})
# print("returned doc :", returned_doc)
#
# print("gettting doc by string object_id")
# object_id_as_str = str(object_id)
# returned_doc_2 = collection.find_one({"_id": object_id_as_str})  # returns None
# print("returned doc_2 :", returned_doc_2)


print("\nprogram ended...")