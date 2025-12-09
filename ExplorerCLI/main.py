# Escolha a API que deseja trabalhar 
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def cli(key, q):
    endpoint = 'http://api.weatherapi.com/v1/current.json'

    paramentros_api = {
        "key" : f"{key}",
        "q": f"{q}"
    }

    #requisicao

    response = requests.get(endpoint, params=paramentros_api)

    if response.status_code == 200:
        print("Sucesso! Requisição OK.")
    else:
        print(f'Erro na requisição. Código: {response.status_code}')
    
    
    try:
        dados = response.json()
        print(f'A temperatura atual de {q}: {dados["current"]["temp_c"]}')
    except json.JSONDecodeError:
        print('Erro de parsing!')
    except KeyError:
        print('Não foi possível encontrar as informações da cidade desejada. Digite novamente')
        
        
#print(cli("API_KEY", "São Paulo"))
if __name__=='__main__':
    API_KEY = os.getenv('WEATHER_API_KEY')
    
    if not API_KEY:
        print('Erro: A chave "WEATHER_API_KEY" não foi carregada. Configyre o .env')
        exit()
        
    while True:
        print('\nExploreCLI')
        q = str(input('Digite o nome da cidade que você deseja saber a temperatura(E digite "exit" para sair): ')).upper()
        if q == 'EXIT':
            print('Até mais, User!')
            break
        else:
            cli(API_KEY, f"{q}")  # Usando minha chave API para gerenciar o sistema
        
    