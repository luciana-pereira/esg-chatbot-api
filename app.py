from flask import Flask
from routes.chatbot_routes import chatbot_bp

app = Flask(__name__)
app.register_blueprint(chatbot_bp)

if __name__ == '__main__':
    app.run(debug=True)