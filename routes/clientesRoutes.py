from controllers.clientesController import clientesController,clientesHtmlController

def clientesRoutes(app):
    app.route('/clientesHTML', methods = ['GET'])(clientesHtmlController)
    app.route('/clientes', methods = ['GET', 'POST','PUT','DELETE'])(clientesController)