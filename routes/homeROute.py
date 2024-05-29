from controllers.homeController import homeController

def homeRoutes(app):
    app.route('/', methods = ['POST', 'GET'])(homeController) 