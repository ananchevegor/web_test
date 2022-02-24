import jinja2
from aiohttp import web
from .routes import setup_routes
import aiohttp_jinja2
import json





async def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('web', 'template'))
    setup_routes(app)
    return app