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
(.venv)> pip install rasa
```

# Utilização

## Inicialização do serviço do bot

```
(.venv)> rasa run --cors "*"
```

## Interação com o bot

Abrir o arquivo ``bot_front\index.html``
