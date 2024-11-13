import pandas as pd
import json
from repository import registro_repository


def importa_registros():
    print("=" * 50)
    print("Importando registros")
    print("=" * 50)

    with open('../assets/registry.json', 'r') as arquivo:
        dados = json.load(arquivo)

        for registro in dados:
            print(registro)
            registro_repository.criar(registro)
            
    print("Registro cadastrado com sucesso!!!")

def listar_registro():
    print("=" * 50)
    print("Listando registros de estoque")
    print("=" * 50)

    registros = registro_repository.listar();

    if registros:
        print(pd.DataFrame.from_records(registros, columns=['id', 'k', 'p', 'lrd', 'humidity', 'temperature', 'relay', 'data'], index='id'))
    else:
        print("Não existe registros")
