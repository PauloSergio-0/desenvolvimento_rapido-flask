from database.sessao import db

class Transacao(db.Model):
    __tablename__ = 'transacao'
    Id = db.Column(db.Integer(), primary_key =True)
    conta = db.Column(db.String(20), nullable = False)
    agencia = db.Column(db.String(10), nullable = False)
    texto = db.Column(db.String(), nullable = True)
    valor = db.Column(db.Float(), nullable = True)
    excluido = db.Collumn(db.Boolean(), default = False)

