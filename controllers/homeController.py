from models.cliente import Clientes
from flask import render_template
def homeController():
    try:
        user = Clientes("Maria Joana","1234")
        return render_template("home.html", user=user)
    except Exception as e:
        return f"Erro:{e}"