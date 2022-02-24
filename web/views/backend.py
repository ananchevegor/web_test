from aiohttp import web
import json
import requests
from bson.objectid import ObjectId


from web_test.web.database.database import collections, db


async def find_by_id():
    obj_id_to_find = ''
    [i for i in db.neo_nodes.find({"_id": ObjectId(obj_id_to_find)})]


# async def create_new_product(request):
#     phone = {
#         "name": "test",
#         "price": 2000
#     }
#     response = requests.post('http://127.0.0.1:80/new_phone', data=phone)









