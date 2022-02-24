from .views import frontend
from .views import backend
from .database import database
import json





def setup_routes(app):
    # app.router.add_post('/product', backend.new_product)
    app.router.add_route('GET', '/', frontend.index)
    #app.router.add_post('/new_phone', backend.create_new_product)
