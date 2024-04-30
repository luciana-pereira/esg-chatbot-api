from flask import Flask
from flask_restful import Api
from flask_cors import CORS  # Importe o pacote Flask-CORS
from routes.chatbot_routes import ChatbotResource

app = Flask(__name__)
api = Api(app)

# Adicione os recursos da API
api.add_resource(ChatbotResource, '/chatbot')

# Configuração do CORS
CORS(app, origins=['https://portal-esg.vercel.app'])
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
