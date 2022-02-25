from bson.objectid import ObjectId
from aiohttp import web
import json
from web_test.web.database.database import collections, db


async def create_new_plagin(request):
    plagins = {
        "_id": "123kjh12kl3j",
        "name": "Philips",
        "price": 20000
    }
    collections.insert_one(plagins)
    return web.json_response(plagins)

async def find_by_name(request):
    name = request.query["name"]
    insert = collections.find({'name': name})
    lst = list(insert)
    json_data = json.dumps(lst, indent=2, default=str)
    return web.Response(text=json_data)

async def find_by_color(request):
    color = request.query["color"]
    insert = collections.find({'color': color})
    lst = list(insert)
    json_data = json.dumps(lst, default=str)
    return web.Response(text=json_data)



