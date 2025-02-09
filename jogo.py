# jogo.py

import random

def calcular_mao(mao):
    valores = {"ás": 1, "as": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 0, "j": 0, "q": 0, "k": 0}
    soma = sum([valores[card.lower()] for card in mao])
    return soma % 10

def jogar_rodada(mao_jogador1, mao_jogador2):
    resultado = "Empate"
    soma_jogador1 = calcular_mao(mao_jogador1)
    soma_jogador2 = calcular_mao(mao_jogador2)
    if soma_jogador1 > soma_jogador2:
        resultado = "Jogador1"
    elif soma_jogador2 > soma_jogador1:
        resultado = "Jogador2"
    return resultado, soma_jogador1, soma_jogador2

def gerar_mao():
    cartas = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return random.sample(cartas, 2)

def acao_jogador(mao, decisao):
    if decisao == "pegar":
        mao.append(random.choice(["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]))
    return mao