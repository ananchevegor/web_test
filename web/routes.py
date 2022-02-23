from .views import frontend
from aiohttp import web


def setup_routes(app):
    app.router.add_route('GET', '/', frontend.index)
