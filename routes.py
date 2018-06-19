from aiohttp.hdrs import METH_GET, METH_PUT, METH_ANY, METH_POST
from controller import Category


# list of a routes in application and it's handlers
routes = [
    (METH_GET,      '/category/{ids}',    Category)
]


# add all defined rout from variable `routes` into web application
def setup_routes(app):
    for route in routes:
        # setup base http routes
        app.router.add_route(route[0], route[1], route[2])

