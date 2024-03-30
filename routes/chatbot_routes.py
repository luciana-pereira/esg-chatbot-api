from flask import Blueprint, request, jsonify
from flask_restful import Resource, reqparse
from chatbot.chatbot import Chatbot

# Crie a instância do Chatbot com palavras-chave relacionadas ao aplicativo ESEG
app_keywords = ['eseg', 'aplicativo', 'duvida', 'ajuda']
chatbot = Chatbot(app_keywords)

# Defina as rotas do Blueprint chatbot_bp
chatbot_bp = Blueprint('chatbot', __name__)

class ChatbotResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, required=True, help='Mensagem do usuário não pode ser vazia')
        args = parser.parse_args()
        message = args['message']
        response = chatbot.get_response(message)
        return jsonify({'response': response})

# Adicione o recurso ChatbotResource à rota '/chatbot'
chatbot_bp.add_url_rule('/chatbot', view_func=ChatbotResource.as_view('chatbot_resource'))

# Se preferir, pode manter a rota original
# @chatbot_bp.route('/chatbot', methods=['POST'])
# def chatbot_endpoint():
#     data = request.json
#     message = data.get('message')
#     response = chatbot.get_response(message)
#     return jsonify({'response': response})
