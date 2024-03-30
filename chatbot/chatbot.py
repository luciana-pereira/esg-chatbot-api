import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class Chatbot:
    def __init__(self, app_keywords=None):
        self.responses = [
            {"question": "oi", "ola" "answer": "Olá! Como posso ajudar?"},
            {"question": "tchau", "answer": "Até logo!"},
            {"question": "como você está?", "answer": "Estou bem, obrigado por perguntar!"},
            {"question": "qual é o seu nome?", "answer": "Meu nome é Chatbot. Como posso ajudar?"},
        ]
        self.stop_words = set(stopwords.words('portuguese'))
        self.lemmatizer = WordNetLemmatizer()
        self.app_keywords = app_keywords if app_keywords else []

    def preprocess(self, text):
        tokens = word_tokenize(text.lower())  # Tokenização e conversão para minúsculas
        filtered_tokens = [token for token in tokens if token.isalpha() and token not in self.stop_words]  # Remover stopwords e pontuação
        lemmatized_tokens = [self.lemmatizer.lemmatize(token, self.get_wordnet_pos(tag)) for token, tag in nltk.pos_tag(filtered_tokens)]  # Lematização
        return lemmatized_tokens

    def get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN

    def get_response(self, message):
        preprocessed_message = self.preprocess(message)
        # Verificar se a mensagem contém palavras-chave relacionadas ao aplicativo ESEG
        for keyword in self.app_keywords:
            if keyword in preprocessed_message:
                return "Sua pergunta relacionada ao aplicativo ESEG foi recebida. Em breve, um de nossos representantes irá lhe ajudar."
        # Procurar respostas gerais
        for qa_pair in self.responses:
            if qa_pair["question"] in preprocessed_message:
                return qa_pair["answer"]
        return "Desculpe, não entendi."

