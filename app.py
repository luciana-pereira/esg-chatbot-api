from flask import Flask
from flask_restful import Api
from routes.chatbot_routes import ChatbotResource

app = Flask(__name__)
api = Api(app)

# Adicione os recursos da API
api.add_resource(ChatbotResource, '/chatbot')

if __name__ == '__main__':
    app.run(debug=True)
