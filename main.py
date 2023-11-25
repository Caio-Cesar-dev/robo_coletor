from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from time import sleep
import pandas as pd

def coleta_dados():
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    empresas = ['PETR3.SA', 'BBDC4.SA', 'VALE3.SA', 'BBAS3.SA', 'ABEV3.SA']
    valores = list()
    data_hora = list()

    for empresa in empresas:
        driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

        input_busca = driver.find_element(By.ID, 'filled-normal')
        input_busca.send_keys(empresa)
        sleep(2)
        input_busca.send_keys(Keys.ENTER)
        sleep(1)

        span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
        cotacao_valor = span_val.text

        valores.append(cotacao_valor)
        data_hora.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

    dados = { 
        'empresa': empresas,
        'valor': valores,
        'data_hora': data_hora,
    }
    
    return dados


def cria_excel(dados, file_name):
    df_empresas = pd.DataFrame(dados)
    df_empresas.to_excel(file_name, index=False)

#Chamando aas funções
dados = coleta_dados()
cria_excel(dados, './empresas_acoes.xlsx')