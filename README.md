# pos_chatbots

O objetivo deste repositório é disponibilizar um chatbot construído com o Rasa e Rasa X para a disciplina de Chatbos e Introdução à NLP do curso de Pós-Graduação em Data Science da Universidade Regional de Blumenau (FURB).

Alunos:
- Guilherme Cristiano Goll
- Fernanda Krieger da Silva Beber

O Bot: seu nome é Hermann, em homenagem ao fundador do município de Blumenau - SC, e prevê a disponibilização de alguns serviços (mock) disponíveis na Praça do Cidadão. Estes serviços serão mais detalhados na seção de [Utilização](#Utilização) desta documentação.

# Setup

Observação: este projeto foi criado utilizando o Python 3.8.8. Por questões de compatibilidade, sugere-se utilizar a mesma release para testes e parte-se da premissa de que o mesmo já se encontra instalado.

## Criar e ativar um ambiente virtual

```
> python -m venv .venv   
> ./.venv/Scripts/activate
```
## Instalação das dependências

```
(.venv)> pip install -r requirements.txt
```

# Treinamento do modelo

## Para treinamento do modelo deve-se executar o comando abaixo:

Obs: é necessário estar no diretório ``rasa_bot`` para que o comando abaixo funcione.
```
(.venv)> rasa train --force
```

# Utilização

## Inicialização do servidor de ações customizadas (custom action server)

Este servidor é responsável por permitir a chamada de APIs, entre outras funções. Em outras palavras, ele executará o arquivo ``actions.py``.

Obs: é necessário estar no diretório ``rasa_bot`` para que o comando abaixo funcione.

```
(.venv)> rasa run actions
```

## Inicialização do serviço do bot

Obs: é necessário estar no diretório ``rasa_bot`` para que o comando abaixo funcione.

```
(.venv)> rasa run --cors "*" -m models --endpoints endpoints.yml
```

## Inicializaçao do serviço da API

Esta API utiliza o Flask e é bastante simples de ser executada:

Obs: é necessário estar no diretório raiz do repositório para que o comando abaixo funcione.

```
(.venv)> python .\api\api.py
```

## Interação com o bot

Abrir o arquivo ``bot_front\index.html`` com o navegador e iniciar a conversa.
