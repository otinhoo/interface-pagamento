import os

def formatar_nome(nome):
    return nome.title()

def formatar_numero_cartao(numero):
    return f"{numero[:4]}.{numero[4:8]}.{numero[8:12]}.{numero[12:]}"

def formatar_validade(validade):
    return f"{validade[:2]}\\{validade[2:]}"

def armazenar_dados(nome, numero_cartao, validade, cvv):
    dados = {
        "Nome Impresso no Cartão": formatar_nome(nome),
        "Número do Cartão": formatar_numero_cartao(numero_cartao),
        "Validade": formatar_validade(validade),
        "CVV": cvv
    }

    pasta_destino = "dados_pagamento"

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    arquivo_destino = os.path.join(pasta_destino, "dados.txt")

    with open(arquivo_destino, "a") as arquivo:
        arquivo.write(str(dados))
        arquivo.write("\n")

    print("Dados de pagamento armazenados com sucesso.")

# Obtendo os dados do usuário
nome = input("Nome Impresso no Cartão: ")
numero_cartao = input("Número do Cartão: ")
validade = input("Validade (ddmm): ")
cvv = input("CVV: ")

# Armazenando os dados
armazenar_dados(nome, numero_cartao, validade, cvv)
