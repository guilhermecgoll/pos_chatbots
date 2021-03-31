# pos_chatbots

Observação: este projeto foi criado utilizando o Python 3.8.8. Por questões de compatibilidade, sugere-se utilizar a mesma release para testes e parte-se da premissa de que o mesmo já se encontra instalado.

# Setup:

## Criar e ativar um ambiente virtual

```
> python -m venv .venv   
> ./.venv/Scripts/activate
```
## Instalação das dependências

```
(.venv)> pip install rasa
```

## Inicialização do serviço do bot

```
(.venv)> rasa run --cors "*"
```

## Interação com o bot

Abrir o arquivo ``bot_front\index.html``