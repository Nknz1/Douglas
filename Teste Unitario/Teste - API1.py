from metodos import *
import datetime
import requests
import json
import os

# Exclui e cria o arquivo de log

try:
    os.remove("execucaoApi1.log")
except:
    open('execucaoApi1.log','x')

def teste_soma():

    # Abre o arquivo para gravação
    with open('execucaoApi1.log','a+') as isfile:

        # Grava informações sobre o teste
        isfile.write('{} - ------------------------------------------------- TESTE UNITARIOS -------------------------------------------------\n'.format(datetime.datetime.now()))
        isfile.write('{} - TESTE 1\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE SOMA - Enviar no campo ACAO o valor SOMA com os numeros 4,3,2,1 e esperar o retorno 10.0****\n'.format(datetime.datetime.now()))

        # Corpo da requisição
        body = {
                "acao":"soma",
                "numeros": [4,3,2,1]
                }

        # Envia a requisição post e coloca o retorno em uma variavel
        post = post_request(json.dumps(body))

        # Transforma a response em um objeto json
        entities = post.json()

        # pega o valor do retorno
        retorno = entities['Total']

        if(post.status_code == 200 and retorno == 10.0):
            isfile.write('{} - TESTE SOMA - Status code = {} * Valor Esperado: 10.0 - Valor retornado : {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')
        else:
            isfile.write(' \n')
            isfile.write('{} - (ERROR)TESTE SOMA - Status code = {} * Valor Esperado: 10.0 - Valor retornado : {}\n'.format(datetime.datetime.now(),post.status_code,retorno))

def teste_subtracao():

    # Abre o arquivo para gravação
    with open('execucaoApi1.log','a+') as isfile:

    # Grava informações sobre o teste
        isfile.write('{} - TESTE 2\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE SUBTRACAO - Enviar no campo ACAO o valor SUBTRAI com os numeros 4,3,2,1 e esperar o retorno -2.0****\n'.format(datetime.datetime.now()))

        # Corpo da requisição
        body = {
                "acao":"subtrai",
                "numeros": [4,3,2,1]
                }

        # Envia a requisição post e coloca o retorno em uma variavel
        post = post_request(json.dumps(body))

        # Transforma a response em um objeto json
        entities = post.json()

        # pega o valor do retorno
        retorno = entities['Total']

        if(post.status_code == 200 and retorno == -2.0):
            isfile.write('{} - TESTE SUBTRACAO - Status code = {} * Valor Esperado: -2.0 - Valor retornado : {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')
        else:
            isfile.write(' \n')
            isfile.write('{} - (ERROR)TESTE SUBTRACAO - Status code = {} * Valor Esperado: -2.0 - Valor retornado : {}\n'.format(datetime.datetime.now(),post.status_code,retorno))

def teste_media():

    # Abre o arquivo para gravação
    with open('execucaoApi1.log','a+') as isfile:

    # Grava informações sobre o teste
        isfile.write('{} - TESTE 3\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE MEDIA - Enviar no campo ACAO o valor MEDIA com os numeros 2,4 e esperar o retorno 3.0****\n'.format(datetime.datetime.now()))

        # Corpo da requisição
        body = {
                "acao":"media",
                "numeros": [2,4]
                }

        # Envia a requisição post e coloca o retorno em uma variavel
        post = post_request(json.dumps(body))

        # Transforma a response em um objeto json
        entities = post.json()

        # pega o valor do retorno
        retorno = entities['Total']

        if(post.status_code == 200 and retorno == 3.0):
            isfile.write('{} - TESTE MEDIA - Status code = {} * Valor Esperado: 3.0 - Valor retornado : {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')
        else:
            isfile.write(' \n')
            isfile.write('{} - (ERROR)TESTE MEDIA - Status code = {} * Valor Esperado: 3.0 - Valor retornado : {}\n'.format(datetime.datetime.now(),post.status_code,retorno))

def teste_total():

    # Abre o arquivo para gravação
    with open('execucaoApi1.log','a+') as isfile:

    # Grava informações sobre o teste
        isfile.write('{} - TESTE 4\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE TOTAL - Enviar no campo ACAO o valor MEDIA com os numeros 5,4,3,2,2 e esperar o retorno 5****\n'.format(datetime.datetime.now()))

        # Corpo da requisição
        body = {
                "acao":"total",
                "numeros": [5,4,3,2,2]
                }

        # Envia a requisição post e coloca o retorno em uma variavel
        post = post_request(json.dumps(body))

        # Transforma a response em um objeto json
        entities = post.json()

        # pega o valor do retorno
        retorno = entities['Total']

        if(post.status_code == 200 and retorno == 5):
            isfile.write('{} - TESTE TOTAL - Status code = {} * Valor Esperado: 5 - Valor retornado : {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')
        else:
            isfile.write(' \n')
            isfile.write('{} - (ERROR)TESTE TOTAL - Status code = {} * Valor Esperado: 5 - Valor retornado : {}\n'.format(datetime.datetime.now(),post.status_code,retorno))

def teste_campo_acao_vazio():

    # Abre o arquivo para gravação
    with open('execucaoApi1.log','a+') as isfile:

    # Grava informações sobre o teste
        isfile.write('{} - TESTE 5\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE CAMPO ACAO VAZIO - Enviar no campo ACAO sem VALOR e esperar o retorno "Campo Obrigátorio, por favor preencha"****\n'.format(datetime.datetime.now()))

        # Corpo da requisição
        body = {
                "acao":" ",
                "numeros": [5,4,3,2,2]
                }

        # Envia a requisição post e coloca o retorno em uma variavel
        post = post_request(json.dumps(body))
        retorno = ""

        try:
            # Transforma a response em um objeto json
            entities = post.json()
            # pega o valor do retorno
            retorno = entities['mensagem']
        except:
             isfile.write('{} - (ERROR)TESTE ACAO VAZIO - A Api nao contem um json como retorno ainda !\n'.format(datetime.datetime.now()))
             isfile.write(' \n')


        if(post.status_code == 422 and retorno == "Campo obrigatório vazio, preencha por favor"):
            isfile.write('{} - TESTE ACAO VAZIO - Status code = {} * Mensagem: {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')

        if(post.status_code == 422 and retorno != "Campo obrigatório vazio, preencha por favor"):
            isfile.write('{} - (ERROR)TESTE ACAO VAZIO - A API esta com o json de retorno diferente do proposto ! - Status code = {} * Mensagem: {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')

        if(post.status_code != 422 and retorno == "Campo obrigatório vazio, preencha por favor"):
            isfile.write('{} - (ERROR)TESTE ACAO VAZIO - A API esta com o status code diferente do proposto ! - Status code = {} * Mensagem: {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')

def teste_campo_numeros_vazio():

    # Abre o arquivo para gravação
    with open('execucaoApi1.log','a+') as isfile:

    # Grava informações sobre o teste
        isfile.write('{} - TESTE 6\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE CAMPO NUMEROS VAZIO - Enviar no campo NUMEROS sem VALOR e esperar o retorno "Campo Obrigátorio, por favor preencha"****\n'.format(datetime.datetime.now()))

        # Corpo da requisição
        body = {
                "acao":"soma",
                "numeros": ""
                }

        # Envia a requisição post e coloca o retorno em uma variavel
        post = post_request(json.dumps(body))
        retorno = ""

        try:
            # Transforma a response em um objeto json
            entities = post.json()

            # pega o valor do retorno
            retorno = entities['mensagem']
        except:
             isfile.write('{} - (ERROR)TESTE NUMEROS VAZIO - A Api nao contem um json como retorno ainda !\n'.format(datetime.datetime.now()))
             isfile.write(' \n')

        if(post.status_code == 422 and retorno == "Campo obrigatório vazio, preencha por favor"):
            isfile.write('{} - TESTE NUMEROS VAZIO - Status code = {} * Mensagem: {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')

        if(post.status_code == 422 and retorno != "Campo obrigatório vazio, preencha por favor"):
            isfile.write('{} - (ERROR)TESTE NUMEROS VAZIO - A API esta com o json de retorno diferente do proposto ! - Status code = {} * Mensagem: {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')

        if(post.status_code != 422 and retorno == "Campo obrigatorio vazio, preencha por favor"):
            isfile.write('{} - (ERROR)TESTE NUMEROS VAZIO - A API esta com o status code diferente do proposto ! - Status code = {} * Mensagem: {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')

def teste_param_nao_existe():

    # Abre o arquivo para gravação
    with open('execucaoApi1.log','a+') as isfile:

    # Grava informações sobre o teste
        isfile.write('{} - TESTE 7\n'.format(datetime.datetime.now()))
        isfile.write('{} - Iniciando TESTE...\n'.format(datetime.datetime.now()))
        isfile.write('{} - ****TESTE PARAM INEXISTENTE - Enviar no campo ACAO um VALOR ERRADO e esperar o retorno "OPERAÇÃO INVÁLIDA"****\n'.format(datetime.datetime.now()))

        # Corpo da requisição
        body = {
                "acao":"teste1",
                "numeros": [5,4,3,2,2]
                }

        # Envia a requisição post e coloca o retorno em uma variavel
        post = post_request(json.dumps(body))
        retorno = ""

        try:
            # Transforma a response em um objeto json
            entities = post.json()

            # pega o valor do retorno
            retorno = entities['mensagem']
        except:
             isfile.write('{} - (ERROR)TESTE PARAM INEXISTENTE - A Api nao contem um json como retorno ainda !\n'.format(datetime.datetime.now()))
             isfile.write(' \n')

        if(post.status_code == 422 and retorno == "OPERAÇÃO INVÁLIDA"):
            isfile.write('{} - TESTE PARAM INEXISTENTE - Status code = {} * Mensagem: {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')

        if(post.status_code == 422 and retorno != "OPERAÇÃO INVÁLIDA"):
            isfile.write('{} - (ERROR)TESTE PARAM INEXISTENTE - A API esta com o json de retorno diferente do proposto ! - Status code = {} * Mensagem: {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')

        if(post.status_code != 422 and retorno == "OPERAÇÃO INVÁLIDA"):
            isfile.write('{} - (ERROR)TESTE PARAM INEXISTENTE - A API esta com o status code diferente do proposto ! - Status code = {} * Mensagem: {}\n'.format(datetime.datetime.now(),post.status_code,retorno))
            isfile.write(' \n')


teste_soma()
teste_subtracao()
teste_media()
teste_total()
teste_campo_acao_vazio()
teste_campo_numeros_vazio()
teste_param_nao_existe()


