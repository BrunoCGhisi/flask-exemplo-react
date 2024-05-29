from flask import request
from database.db import db
from models.cliente import Clientes
from flask import render_template

def clientesHtmlController():
    if request.method == 'GET':
        return render_template('clientesHTML.html')

def clientesController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            user = Clientes(data['nome'], data['senha'], data['cargos_id'])
            db.session.add(user)
            db.session.commit()
            return 'Usuario criado com sucesso',200
        except Exception as e: 
            return 'O usuario nao foi criado. Erro: {}'.format(str(e)),405
    elif request.method == 'GET': 
        try:
            data = Clientes.query.all()
            print([cliente.to_dict() for cliente in data ])
            teste = {'clientes':[cliente.to_dict() for cliente in data ]}
            return teste, 200
            return render_template('clientes.html', data = {'clientes':[cliente.to_dict() for cliente in data ]})
        except Exception as e:
            return 'O usuario nao foi encontrado. Erro: {}'.format(str(e)),405
    elif request.method == "PUT":
        try:
            data = request.get_json()
            put_cliente_id = data["id"]
            cliente = Clientes.query.get(put_cliente_id)
            if cliente is None:
                return{'Error cliente não encontrado'}, 404
            cliente.nome = data.get('nome', cliente.nome)
            cliente.senha = data.get('senha', cliente.senha)
            db.session.commit()
            return 'vvsd',202
        except Exception as e:
            return 'Não foi possivel atualizar o ususario {}'.format(str(e))
    elif request.method == "DELETE":
        try:
            data = request.get_json()
            delete_cliente_id = data["id"]
            cliente = Clientes.query.get(delete_cliente_id)
            if cliente is None:
                return {'error':'Cliente nao encontrado'}, 404
            db.session.delete(cliente)
            db.session.commit()
            return 'cliente deletado com sucesso',202
        except Exception as e:
            return 'Não foi possivel deletar o ususario'