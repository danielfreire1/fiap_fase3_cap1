import types
from registro import *

def create_menu():

    return {
        "Importa" : importa_registros,
        "Listar": listar_registro,
        "Sair": sair
    }


def show_menu_principal():
    show_menu(create_menu())


def show_menu(opcoes: dict, opcao_parente=None):

    print("=" * 50)
    print("Opções:")
    for index, (key, _) in enumerate(opcoes.items()):
        print(f"{index} - {key}")

    opcao_selecionada = ""
    while not opcao_selecionada.isnumeric() or int(opcao_selecionada) >= len(opcoes):
        opcao_selecionada = input("Informe o número da opção desejada: ")

    opcao_selecionada, valor_selecionado = list(opcoes.items())[int(opcao_selecionada)]

    if not valor_selecionado:
        return

    if isinstance(valor_selecionado, dict):
        show_menu(valor_selecionado, opcao_selecionada)
    elif isinstance(valor_selecionado, types.FunctionType):
        if opcao_parente in ["Insumos", "Fertilizantes", "Pesticidas"]:
            valor_selecionado(opcao_parente)
        else:
            valor_selecionado()

    show_menu(opcoes, opcao_parente)


def sair():
    print("FINALIZANDO...")
    quit()