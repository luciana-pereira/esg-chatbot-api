# ESG Chatbot API

A API de Chatbot ESG, é uma API desenvolvida em Python com o framework Flask, projetada para fornecer funcionalidades de chatbot aos usuários, especialmente para ajudar a responder dúvidas e fornecer suporte aos usuários da  plataforma ESG Game.

## Objetivo

O objetivo desta API é fornecer uma interface simples para interagir com o chatbot, permitindo que os usuários enviem mensagens e recebam respostas relevantes. A API é alimentada por um chatbot desenvolvido com técnicas de Processamento de Linguagem Natural (NLP) para entender as intenções dos usuários e fornecer respostas contextuais.

## Funcionalidades

- Receber mensagens dos usuários e retornar respostas relevantes.
- Priorizar dúvidas relacionadas ao aplicativo ESG usando palavras-chave específicas.
- Utilizar técnicas de NLP para entender a intenção por trás das mensagens dos usuários.
- Fornecer respostas contextualizadas com base nas mensagens recebidas.

## Instalação

1. Clone este repositório::

```bash
git clone https://github.com/seu-usuario/esg-chatbot-api.git

```

2. Instale as dependências:

```bash
cd esg-chatbot-api
pip install -r requirements.txt

```

3. Execute o servidor:

```bash
python app.py

```

## Utilização
#### Enviar uma mensagem para o chatbot
Envie uma solicitação POST para o endpoint /chatbot com o corpo da solicitação contendo a mensagem do usuário:

```bash
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"message": "Qual é o horário de funcionamento?"}'

```

#### Resposta esperada
```json
{
  "response": "O horário de funcionamento é das 9h às 18h, de segunda a sexta-feira."
}

```

## Contribuição
Contribuições são bem-vindas! Para sugestões, melhorias ou correções de bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT.
