import requests
import json

def post_request(body):
    # parametros para a requisição
    url = 'http://localhost:8080'
    head = {"Content-Type": "application/json"}
    # envia uma requisição post
    get = requests.post(url,data=body,headers=head)
    
    return get


def get_request(param):

    # envia uma requisição get
    url = "http://localhost:8080/id/{}".format(param)
    get = requests.get(url)
    
    return get

def get_request_nome(param):

    # envia uma requisição get
    url = "http://localhost:8080/nome/{}".format(param)
    get = requests.get(url)
    
    return get

def get_request_salario(param):

    # envia uma requisição get
    url = "http://localhost:8080/salario/{}".format(param)
    get = requests.get(url)
    
    return get

def get_request_all():

    # envia uma requisição get
    url = "http://localhost:8080/"
    get = requests.get(url)
    
    return get


def put_request_id(param,param1):

    # envia uma requisição get
    url = "http://localhost:8080/id/{}".format(param)
    head = {"Content-Type": "application/json"}
    body = {
            "pessoa":{

                        "nome":"{}".format(param1),
                        "idade":55,
                        "salario": 1000.00
                    }
            }
    body = json.dumps(body)
    get = requests.put(url,data=body,headers=head)

    if(get.status_code == 200):
        select = get_request(param)
        entities = select.json()

        if(entities["nome"] == param1):
            return select
        else:
            return False
    
    else:
        return False

def put_request_nome(nome_request,nome_update):

    # envia uma requisição get
    url = "http://localhost:8080/nome/{}".format(nome_request)
    head = {"Content-Type": "application/json"}
    body = {
            "pessoa":{

                        "nome":"{}".format(nome_update),
                        "idade":65,
                        "salario": 1000.00
                    }
            }
    body = json.dumps(body)
    get = requests.put(url,data=body,headers=head)

    if(get.status_code == 200):
        select = get_request_nome(nome_update)
        entities = select.json()

        if(entities[0]["nome"] == nome_update):
            return select
        else:
            return False
    
    else:
        return False
