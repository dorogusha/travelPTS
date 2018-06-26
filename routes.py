from aiohttp.hdrs import METH_GET, METH_PUT, METH_ANY, METH_POST, METH_DELETE
from controller import Category
from controller import User


# list of a routes in application and it's handlers
routes = [
    (METH_GET,      '/category/{ids}',      Category),
    (METH_POST,     '/category',            Category),
    (METH_PUT,      '/category',            Category),
    (METH_DELETE,   '/category/{ids}',      Category),

    (METH_GET,      '/user/{ids}',      User),
    (METH_POST,     '/user',            User),
    (METH_PUT,      '/user',            User),
    (METH_DELETE,   '/user/{ids}',      User)
]


# add all defined rout from variable `routes` into web application
def setup_routes(app):
    for route in routes:
        # setup base http routes
        app.router.add_route(route[0], route[1], route[2])

