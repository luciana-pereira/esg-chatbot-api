import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class Chatbot:
    def __init__(self, app_keywords=None):
        self.responses = [
            {"question": "oi", "answer": "Olá! Como posso ajudar?"},
            {"question": "tchau", "answer": "Até logo!"},
            {"question": "como você está?", "answer": "Estou bem, obrigado por perguntar!"},
            {"question": "Não consigo fazer login", "answer": "Verifique se as informações estão corretas e tente novamente."},
            {"question": "Como faço login?", "answer": "Vá para pagina inicial e inclua seus dados cadastrais nos campos Login e Senha"},
            {"question": "Como faço para recuperar minha senha?", "answer": "Vá à área de Login e clique em Recuperar a senha"},
            {"question": "Posso alterar a minha senha?", "answer": "Claro, basta ir em área de Login e clique em Recuperar a senha"},
            {"question": "Esqueci a minha senha, pode me ajudar?", "answer": "Vá à área de Login e clique em Recuperar a senha"},
            {"question": "Minha senha está segura?", "answer": "Para mais informações, entrar em contato com o nosso suporte através do e-mail:suporte@esggame.com" },
            {"question": "Como faço para excluir a minha conta?", "answer": "Você poderá realizar essa ação a qualquer momento, clicando em Meu Cadastro e Excluir Conta." },
            {"question": "Quanto tempo demora para excluir a minha conta?", "answer": "Imediatamente, após selecionar Excluir Conta na área Meu Cadastro" },
            {"question": "Posso recuperar os meus dados antes de excluir a minha conta?", "answer": "Para mais informações, entrar em contato com o nosso suporte através do e-mail:suporte@esggame.com" },
            {"question": "Como faço o cadastro na plataforma?", "answer": "O cadastro em nossa plataforma é feito na página inicial, clicando no botão Cadastre-se" },
            {"question": "Preciso de ajuda para me cadastrar, pode me ajudar?", "answer": "Sim, você deve clicar em Cadastre-se e Sou novo usuário. Importante você precisa concordar com a nossa Política de Privacidade, para o cadastro ser finalizado com sucesso." },
            {"question": "Meus dados de cadastro estão incorretos, como posso alterá-lo?", "answer": "Faça o login em nossa plataforma e clique em Meu Cadastro atualize os campos incorretos e clique em Salvar" },
            {"question": "Para receber os coins e prêmios, meu cadastro precisa estar completo?", "answer": "Sim, para poder receber os coins, seu cadastro deverá estar completo para que os Coins sejam creditados em sua conta corretamente."},
            {"question": "Como faço para ganhar Coins?", "answer": "Você pode ganhar Coins fazendo as atividades listadas na plataforma."},
            {"question": "Como posso ganhar mais Coins?", "answer": "Por enquanto só fazendo as atividades listadas na plataforma"},
            {"question": "Os Coins têm tempo para expirar?", "answer": "Não, as Coins serão mantidas."},
            {"question": "Os Coins demoram para aparecer na conta após a atividade ser concluída?", "answer": "Elas aparecem quando a atividade é concluída."},
            {"question": "Como resgato as minhas premiações?", "answer": "Vá à área de “premiações”, escolha a premiação de sua preferência."},
            {"question": "Quanto tempo para a premiação chegar ao seu destino?", "answer": "Depende dos serviços de entrega. Se preferir, fale diretamente com o suporte pelo e-mail: suporte@esggame.com"},
            {"question": "A premiação é reembolsável?", "answer": "Sim, apenas para os casos em que a premiação esteja com defeito de fabricação, entre em contato diretamente com o suporte pelo e-mail:suporte@esggame.com"},
            {"question": "Como eu posso ativar o leitor de tela?", "answer": "Em desenvolvimento"},
            {"question": "Como posso usar o Zoom na página", "answer": "Em desenvolvimento"},
            {"question": "Como faço para entrar em contato com o suporte do site?", "answer": "Nosso suporte ao cliente, funciona apenas em dias úteis, por meio do e-mail: suporte@esggame.com"},
            {"question": "Esse site é seguro? ", "answer": "Se desejar informações mais detalhadas, nos envie um e-mail com suas dúvidas, que responderemos suas dúvidas. suporte@esggame.com"},
            {"question": "Qual a História de vocês", "answer": "Somos um projeto criado na FIAP visando ajudar pessoas e o meio ambiente de uma forma didática e divertida. "},
            {"question": "Por que essa plataforma é um game?", "answer": "Foi uma ideia que tivemos, para a plataforma ser de alguma forma divertida e servisse a sua função."},
            {"question": "Posso deixar um comentário numa ação já realizada?", "answer": "Acesse o Feed escolha um Post e registre seus comentários para os usuários visualizarem." },
            {"question": "Onde encontro comentários dos meus amigos nas ações que realizei?", "answer": "Para encontrar os comentários dos seus amigos Acesse o Feed e Atividades, onde encontrará os respectivos comentários." },
            {"question": "Gostaria de excluir uma ação realizada recentemente, como faço?", "answer": "Clique na postagem que deseja excluir e poderá visualizar um ícone com 3 pontos, onde poderá excluir a postagem, mas ao realizar essa ação, não poderá ser visualizada novamente por nenhum usuário. Caso tenha clicado por engano, entre em contato conosco pelo e-mail: suporte@esggame.com"},
            {"question": "Como posso mudar a minha foto ", "answer": "Sim, faça o login em nossa plataforma e clique em Meu cadastro Foto e clique em Salvar" },
            {"question": "Gostarias de mudar o meu e-mail", "answer": "Sim, faça o login emnossa plataforma e clique em Meu Cadastro E-mail e clique em Salvar" },
            {"question": "Como posso mudar o meu nome", "answer": "Você não poderá alterar o meu Nome nome e sobrenome, apenas o Como gostaria  de ser chamado para essa alteração faça o  login em nossa  plataforma e clique em Meu Cadastro Como gostaria de ser chamado e clique em Salvar" },
            {"question": "Como encontrar amigos? ", "answer": "Em desenvolvimento!"},
            {"question": "Como faço para encontrar uma página? ", "answer": "Em desenvolvimento!"},
            {"question": "Como fazer um Post?  ", "answer": "Em desenvolvimento!"},
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
