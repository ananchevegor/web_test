from aiohttp import web
from aiohttp_jinja2 import template
import json

async def headle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj))


async def new_product(request):
    try:
        product = request.query['product']
        print("Creating new product: " + product)
        response_obj = {'status' : 'success'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status':'error', 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)