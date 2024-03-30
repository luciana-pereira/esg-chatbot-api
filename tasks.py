from celery import Celery
from chatbot.chatbot import process_message  # Importa a função de processamento do chatbot

# Crie uma instância de Celery
celery = Celery(__name__)

# Configuração do Celery
celery.conf.broker_url = 'redis://localhost:6379/0'
celery.conf.result_backend = 'redis://localhost:6379/0'

# Tarefa do Celery para processar mensagens do chatbot
@celery.task
def process_chat_message(message):
    """
    Tarefa do Celery para processar mensagens do chatbot.

    Args:
        message (str): A mensagem a ser processada pelo chatbot.
    
    Returns:
        str: Resposta do chatbot.
    """
    # Chama a função de processamento do chatbot
    response = process_message(message)
    return response
