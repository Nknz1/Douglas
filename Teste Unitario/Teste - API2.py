from metodos import *
import datetime
import requests
import json
import os

# Exclui e cria o arquivo de log

try:
    os.remove("execucaoApi2.log")
except:
    open('execucaoApi2.log','x')

def teste_select_id(parametro):

    # Abre o arquivo para gravação
    with open('execucaoApi2.log','a+') as isfile:

        # Grava informações sobre o teste
        isfile.write('{} - ------------------------------------------------- TESTE UNITARIOS -------------------------------------------------\n'.format(datetime.datetime.now()))
        isfile.write('{} - TESTE 1\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE SELECT POR ID - Retornar o usuario com ID 1 registrado no banco de dados****\n'.format(datetime.datetime.now()))

        # Envia a requisição get e coloca o retorno em uma variavel
        post = get_request(parametro)

        # Transforma a response em um objeto json
        entities = post.json()

        if(post.status_code == 200 and entities != ""):
            isfile.write('{} - TESTE SELECT POR ID - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')
        if(post.status_code != 200):
            isfile.write(' \n')
            isfile.write('{} - (ERROR)TESTE SELECT POR ID - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))

def teste_select_errado_id(parametro):

    # Abre o arquivo para gravação
    with open('execucaoApi2.log','a+') as isfile:

        # Grava informações sobre o teste
        isfile.write('{} - TESTE 2\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE SELECT POR ID ERRADO - Retornar um json falando que o ID não existe****\n'.format(datetime.datetime.now()))

        # Envia a requisição get e coloca o retorno em uma variavel
        post = get_request(parametro)

        try:
            # Transforma a response em um objeto json
            entities = post.json()
        except:
            isfile.write('{} - (ERROR)TESTE SELECT POR ID ERRADO - A Api nao contem um json como retorno ainda !\n'.format(datetime.datetime.now()))
            isfile.write(' \n')

        if(post.status_code == 200 and entities != ""):
            isfile.write('{} - (ERROR)TESTE SELECT POR ID ERRADO - Status code = {} * Json Retornado: {} * A API está retornando um ID que não existe\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')
        if(post.status_code == 422 and entities != ""):
            isfile.write('{} - TESTE SELECT POR ID ERRADO - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

        if(post.status_code != 200 and entities != ""):
            isfile.write('{} - TESTE SELECT POR ID ERRADO - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

def teste_select_all():

    # Abre o arquivo para gravação
    with open('execucaoApi2.log','a+') as isfile:

        # Grava informações sobre o teste
        isfile.write('{} - TESTE 3\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE SELECT ALL - Retornar todos os usuarios cadastrados no DB****\n'.format(datetime.datetime.now()))

        # Envia a requisição get e coloca o retorno em uma variavel
        post = get_request_all()

        try:
            # Transforma a response em um objeto json
            entities = post.json()
        except:
            isfile.write('{} - (ERROR)TESTE SELECT ALL - A Api nao contem um json como retorno ainda !\n'.format(datetime.datetime.now()))
            isfile.write(' \n')

        if(post.status_code == 200 and entities != ""):
            isfile.write('{} - TESTE SELECT ALL - Status code = {} * Json Retornado: {} *\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

        if(post.status_code != 200):
            isfile.write('{} - (ERROR)TESTE SELECT ALL - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

def teste_select_nome(parametro):

    # Abre o arquivo para gravação
    with open('execucaoApi2.log','a+') as isfile:

        # Grava informações sobre o teste
        isfile.write('{} - TESTE 4\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE SELECT POR NOME - Retornar o usuario com NOME registrado no banco de dados****\n'.format(datetime.datetime.now()))

        # Envia a requisição get e coloca o retorno em uma variavel
        post = get_request_nome(parametro)
        entities = ""

        try:
            # Transforma a response em um objeto json
            entities = post.json()
        except:
            isfile.write('{} - (ERROR)TESTE SELECT POR NOME - A Api nao contem um json como retorno ainda !\n'.format(datetime.datetime.now()))
            isfile.write(' \n')

        if(post.status_code == 200 and entities != ""):
            isfile.write('{} - TESTE SELECT POR NOME - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

        if(post.status_code == 404):
            isfile.write(' \n')
            isfile.write('{} - (ERROR)TESTE SELECT POR NOME - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))

def teste_select_errado_nome(parametro):

    # Abre o arquivo para gravação
    with open('execucaoApi2.log','a+') as isfile:

        # Grava informações sobre o teste
        isfile.write('{} - TESTE 5\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE SELECT POR NOME ERRADO - Retornar um json falando que o NOME não existe****\n'.format(datetime.datetime.now()))

        # Envia a requisição get e coloca o retorno em uma variavel
        post = get_request_nome(parametro)
        entities = ""
        try:
            # Transforma a response em um objeto json
            entities = post.json()
            entities['nome']
        except:
            isfile.write('{} - (ERROR)TESTE SELECT POR NOME ERRADO - A Api nao contem um json como retorno ainda !\n'.format(datetime.datetime.now()))
            isfile.write(' \n')

        if(post.status_code == 200 and entities != ""):
            isfile.write('{} - (ERROR)TESTE SELECT POR NOME ERRADO - Status code = {} * Json Retornado: {} * A API está retornando um ID que não existe\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

def teste_select_salario(parametro):

    # Abre o arquivo para gravação
    with open('execucaoApi2.log','a+') as isfile:

        # Grava informações sobre o teste
        isfile.write('{} - TESTE 6\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE SELECT POR SALARIO - Retornar o usuario com SALARIO registrado no banco de dados****\n'.format(datetime.datetime.now()))

        # Envia a requisição get e coloca o retorno em uma variavel
        post = get_request_salario(parametro)

        try:
            # Transforma a response em um objeto json
            entities = post.json()
        except:
            isfile.write('{} - (ERROR)TESTE SELECT POR SALARIO - A Api nao contem um json como retorno ainda !\n'.format(datetime.datetime.now()))
            isfile.write(' \n')

        if(post.status_code == 200 and entities != ""):
            isfile.write('{} - TESTE SELECT POR SALARIO - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

        if(post.status_code != 200):
            isfile.write(' \n')
            isfile.write('{} - (ERROR)TESTE SELECT POR SALARIO - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))

def teste_update_id(parametro,parametro1):

    # Abre o arquivo para gravação
    with open('execucaoApi2.log','a+') as isfile:

        # Grava informações sobre o teste
        isfile.write('{} - TESTE 7\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE UPDATE POR ID - Faz o Update por ID no banco de dados****\n'.format(datetime.datetime.now()))

        # Envia a requisição get e coloca o retorno em uma variavel
        post = put_request_id(parametro,parametro1)

        if(post == False):
            isfile.write('{} - (ERROR)TESTE UPDATE POR ID - Ocorreu um erro ao realizar o update\n'.format(datetime.datetime.now()))
            isfile.write(' \n')

        elif(post.status_code == 200):
            entities = post.json()
            isfile.write('{} - TESTE UPDATE POR ID - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

        elif(post.status_code != 200):
            entities = post.json()
            isfile.write('{} - (ERROR)TESTE UPDATE POR ID - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

        elif(post == False):
            entities = post.json()
            isfile.write('{} - (ERROR)TESTE UPDATE POR ID - Ocorreu um erro ao realizar o update\n'.format(datetime.datetime.now()))
            isfile.write(' \n')

def teste_update_nome(parametro,parametro1):

    # Abre o arquivo para gravação
    with open('execucaoApi2.log','a+') as isfile:

        # Grava informações sobre o teste
        isfile.write('{} - TESTE 8\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE UPDATE POR NOME - Faz o Update por NOME no banco de dados****\n'.format(datetime.datetime.now()))

        # Envia a requisição get e coloca o retorno em uma variavel
        post = put_request_nome(parametro,parametro1)

        if(post == False):
            isfile.write('{} - (ERROR)TESTE UPDATE POR NOME - Ocorreu um erro ao realizar o update\n'.format(datetime.datetime.now()))
            isfile.write(' \n')

        elif(post.status_code == 200):
            entities = post.json()
            isfile.write('{} - TESTE UPDATE POR NOME - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')

        elif(post.status_code != 200):
            entities = post.json()
            isfile.write('{} - (ERROR)TESTE UPDATE POR NOME - Status code = {} * Json Retornado: {}\n'.format(datetime.datetime.now(),post.status_code,entities))
            isfile.write(' \n')



teste_select_id("1")
teste_select_errado_id("2222d")
teste_select_all()
teste_select_nome("Gabriel")
teste_select_errado_nome("dhuashudas")
teste_select_salario(1000.0)
teste_update_id("1","Gaiel")
teste_update_nome("Gaiel","Everton")



