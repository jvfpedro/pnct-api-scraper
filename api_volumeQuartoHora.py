import requests
import pandas as pd
import os
from time import time

dicionario_dias_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10:31,
    11:30,
    12:31,
}

caminho = r"D:\UFSC\00_TCC\trafego\python\volume_hora\postos_quarto"

postos = {"337":    2019,
          "424702": 2022,
          "510":    2019}

for posto, ano in postos.items():

    pasta_posto = os.path.join(caminho, str(posto))
    os.makedirs(pasta_posto, exist_ok=True)

    for mes, dia_max in dicionario_dias_mes.items():
        dia = 1

        while dia <= dia_max:
            url = f"https://servicos.dnit.gov.br/dadospnct/api/VolumeQuartoHora/{posto}?ano={ano}&mes={mes}&dia={dia}&_={time()}"
            response = requests.get(url)
            response.raise_for_status()

            if "dado" in response.json() and response.json()["dado"]:
                data = response.json()["dado"]
                df = pd.DataFrame(data)
                df.to_csv(os.path.join(pasta_posto, f"{mes:02}_{dia:02}.csv"), index=False) 

            else:
                print(f"Nenhum dado disponível para {posto} no dia {dia}/{mes}/{ano}.")

                
            dia += 1