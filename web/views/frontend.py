import aiohttp
from aiohttp import web
from aiohttp_jinja2 import template
import json

@template('index.html')
async def index(request):
    return {}


