from .views import frontend, backend
from aiohttp import web

def setup_routes(app):
    app.add_routes([web.get('/', frontend.index),
                    web.get('/new_plagin', backend.create_new_plagin),
                    web.get('/find_by_name', backend.find_by_name),
                    web.get('/find_by_color', backend.find_by_color),
                    web.get('/find_by_id', backend.find_by_id),
                    web.get('/find_by_id_else', backend.find_by_id_else)])
