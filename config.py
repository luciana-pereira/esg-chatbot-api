import os

class Config:
    # Configurações para acessar o banco de dados do Heroku Postgres
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

