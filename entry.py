import aiohttp
from web import create_app
from aiohttp import web


app = create_app()

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1')
