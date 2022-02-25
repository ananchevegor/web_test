import json
import pymongo
import dns

# создаем подключение к бд
db = pymongo.MongoClient("mongodb+srv://user:JTjF87jpEqFyqlfV@cluster111.66jgc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#выбираем текущую бд, если такой нет, то она сама создасться
current_db = db["phone_db"]

# аналогично коллекция
collections = current_db["phones"]



