from routes.clientesRoutes import clientesRoutes
from routes.homeROute import homeRoutes
from routes.cargosRoutes import cargosRoutes
def routeIndex(app):
    clientesRoutes(app=app)
    homeRoutes(app=app)
    cargosRoutes(app= app)
