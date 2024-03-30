from flask import Blueprint, request, jsonify
from chatbot.chatbot import Chatbot

# Crie a instância do Chatbot com palavras-chave relacionadas ao aplicativo ESEG
app_keywords = ['eseg', 'aplicativo', 'duvida', 'ajuda']
chatbot = Chatbot(app_keywords)

# Defina as rotas do Blueprint chatbot_bp
chatbot_bp = Blueprint('chatbot', __name__)
# chatbot = Chatbot()

@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    data = request.json
    message = data.get('message')
    response = chatbot.get_response(message)
    return jsonify({'response': response})
