from flask import request, jsonify


from database.sessao import db
from model.transacao import Transacao

def register_routes(app):
    @app.route('/cadastrar/transacao', methods = ['POST'])

    def criar_transacao():
        data = request.get_json()

        nova_transacao = Transacao(
            conta = data.get('conta'),
            agencia = data['agencia'],
            texto = data.get('texto', None),
            valor = data['valor']
        )

        db.session.add(nova_transacao)
        db.session.commit()

        return jsonify({"mensagem": 'tresacao realizada'}), 200
    

    @app.route('/listar/transacao', methods = ['GET'])

    def listar_transacao():
        transacoes = Transacao.query.all()
        
        resultado = [{
        'id': transacao.Id,
        'conta':transacao.conta,
        'agencia': transacao.agencia,
        'texto': transacao.texto,
        'valor': transacao.valor
        } for transacao in transacoes]

        return jsonify(resultado), 200
    


    @app.route("/transacao/<int:id>", methods = ['GET'])
    def pegar_transacao(id):
        transacao = Transacao.query.get_or_404(id)

        resultado = transacao.__dict__
        del resultado['sa_instance_state']
        return jsonify({"detail": resultado}), 200
    
    @app.route("/transacao/<int:id>", methods = ['DELETE'])
    def pegar_transacao(id):
        transacao = Transacao.query.get_or_404(id)

        db.session.delete(transacao)

        db.session.commit()
        return jsonify({"detail": "foi"}), 200
    
    
    @app.route("atualizacao/transacao/<int:id>", methods = ['PUT'])
    def pegar_transacao(id):
        data = request.get_json()
        transacao = Transacao.query.get_or_404(id)


        transacao.conta = data.get('conta', transacao.conta)
        transacao.agencia = data.get('agencia', transacao.agencia)
        transacao.texto = data.get('texto', transacao.texto)
        transacao.valor = data.get('valor', transacao.valor)

        db.session.add(transacao)
        db.session.commit()

        return jsonify({"detail": "foi 2"}), 200

    @app.route("/exclusao/logica/transacao/<int:id>", methods = ['PATCH'])
    def pegar_transacao(id):
        data = request.get_json()
        transacao = Transacao.query.get_or_404(id)


        transacao.excluido = data.get('excluido', True.excluido)
        transacao.agencia = data.get('agencia', transacao.agencia)
        transacao.texto = data.get('texto', transacao.texto)
        transacao.valor = data.get('valor', transacao.valor)

        db.session.add(transacao)
        db.session.commit()

        return jsonify({"detail": "foi 2"}), 200