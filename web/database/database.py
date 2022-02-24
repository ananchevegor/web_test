import json
import pymongo
import dns

# создаем подключение к бд
db = pymongo.MongoClient("mongodb+srv://user:JTjF87jpEqFyqlfV@cluster111.66jgc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#выбираем текущую бд, если такой нет, то она сама создасться
current_db = db["phone_db"]

# аналогично коллекция
collections = current_db["phones"]



# открываем json фвйл на чтение, чтобы занести все данные в бд
# with open("A:\pythonLearn\web_test\web_test\web\database\data_database\data_phone.json", 'r', encoding='utf8') as p:
#     obj = json.load(p)
#     ins = collections.insert_many(obj)


