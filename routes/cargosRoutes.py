from controllers.cargosController import cargosController

def cargosRoutes(app):
    app.route('/cargos', methods = ['GET', 'POST'])(cargosController)