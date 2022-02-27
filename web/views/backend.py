from bson.objectid import ObjectId
from aiohttp import web
import json
from web.database.database import collections, db


async def create_new_plagin(request):
    try:
        plagins = {
            "name": "Nokia",
            "color": "black",
            "description": "something",
            "price": 20000
        }
        collections.insert_one(plagins)
        return web.Response(text=json.dumps({'status': 'success'}))
    except Exception as e:
        return web.Response(text=json.dumps({'status': str(e)}))

async def find_by_name(request):
    try:
        name = request.query["name"]
        insert = collections.find({'name': name})
        json_data = json.dumps(list(insert), default=str, indent=2)
        return web.Response(text=json_data)
    except Exception as e:
        return web.Response(text=json.dumps({'status': str(e)}))

async def find_by_color(request):
    try:
        color = request.query["color"]
        insert = collections.find({'color': color})
        json_data = json.dumps(list(insert), default=str, indent=2)
        return web.Response(text=json_data)
    except Exception as e:
        return web.Response(text=json.dumps({'status': str(e)}))

async def find_by_id(request):
    try:
        id = request.query["id"]
        insert = collections.find({'_id': ObjectId(id)}, {'name': True, 'color': True, '_id': False})
        json_data = json.dumps(list(insert), default=str, indent=2)
        return web.Response(text=json_data)
    except Exception as e:
        return web.Response(text=json.dumps({'status': str(e)}))

async def find_by_id_else(request):
    try:
        id = request.query["id"]
        insert = collections.find({'_id': id})
        json_data = json.dumps(list(insert), default=str, indent=2)
        return web.Response(text=json_data)
    except Exception as e:
        return web.Response(text=json.dumps({'status': str(e)}))
