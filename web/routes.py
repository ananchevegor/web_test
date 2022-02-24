from .views import frontend
from .views import backend



def setup_routes(app):
    app.router.add_post('/product', backend.new_product)
    app.router.add_route('GET', '/', frontend.index)