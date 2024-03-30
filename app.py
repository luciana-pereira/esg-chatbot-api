from flask import Flask
from routes.chatbot_routes import chatbot_bp
from config import Config 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(chatbot_bp)

# Configure a aplicação Flask com as configurações definidas em Config
app.config.from_object(Config)

# Inicialize a extensão SQLAlchemy passando a aplicação Flask como argumento
db = SQLAlchemy(app)

# Defina seus modelos de banco de dados usando SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    app.run(debug=True)
