from database.db import db

class Cargos(db.Model):
    def to_dict(self):
        return{
            'id': self.id,
            'nome': self.nome
        }
    id = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    nome = db.Column(db.String(100))

    def __init__(self,nome):
        self.nome = nome