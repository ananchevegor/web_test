from bson.objectid import ObjectId
from aiohttp import web
import json
from web.database.database import collections, db


async def create_new_plagin(request):
    plagins = {
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
    json_data = json.dumps(list(insert), default=str)
    return web.Response(text=json_data)

async def find_by_id(request):
    id = request.query["id"]
    insert = collections.find({'_id': ObjectId(id)})
    json_data = json.dumps(list(insert), default=str)
    return web.Response(text=json_data)

async def find_by_id_else(request):
    id = request.query["id"]
    insert = collections.find({'_id': id})
    lst = list(insert)
    json_data = json.dumps(lst, default=str)
    return web.Response(text=json_data)



