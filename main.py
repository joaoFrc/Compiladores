# main.py

from lexico import tokenizar
from sintatico import Parser, Node
from jogo import jogar_rodada, gerar_mao, acao_jogador
import os

# Variável global para armazenar a árvore de derivação
arvore_derivacao = None

def registrar_arvore_derivacao(arvore):
    if not os.path.exists("registros"):
        os.makedirs("registros")
    with open("registros/log_arvoreDerivacao.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(str(arvore) + "\n\n")

def main():
    global arvore_derivacao
    banca = 1000.00
    mao_jogador1 = []
    mao_jogador2 = []

    while True:
        print(f"\nSaldo atual: R${banca:.2f}")
        if banca <= 0:
            print("\nSua banca acabou. Jogo encerrado!")
            break

        entrada = input("Digite um comando (ex: 'aposta jogador1 100', 'mao', 'jogador1 manter', 'resultado'): ")
        tokens = tokenizar(entrada)

        try:
            parser = Parser(tokens)
            nova_arvore = parser.parse()

            # Adiciona a nova árvore à árvore de derivação global
            if arvore_derivacao is None:
                arvore_derivacao = Node("COMANDO", [nova_arvore])
            else:
                arvore_derivacao.children.append(nova_arvore)

            print("\nÁrvore de Derivação:")
            print(arvore_derivacao)
            registrar_arvore_derivacao(arvore_derivacao)

            if tokens[0] == "aposta":
                tipo_aposta = tokens[1]
                valor_aposta = float(tokens[2])
                if valor_aposta > banca:
                    print("\nVocê não tem dinheiro suficiente para essa aposta.")
                    continue

                banca -= valor_aposta
                mao_jogador1 = gerar_mao()
                mao_jogador2 = gerar_mao()

                print("\nMão do Jogador 1:", mao_jogador1)
                print("Mão do Jogador 2:", mao_jogador2)

            elif tokens[0] in ["jogador1", "jogador2"]:
                jogador = tokens[0]
                decisao = tokens[1]
                if jogador == "jogador1":
                    mao_jogador1 = acao_jogador(mao_jogador1, decisao)
                    print(f"\nJogador 1 decidiu {decisao}. Nova mão:", mao_jogador1)
                else:
                    mao_jogador2 = acao_jogador(mao_jogador2, decisao)
                    print(f"\nJogador 2 decidiu {decisao}. Nova mão:", mao_jogador2)

            elif tokens[0] == "resultado":
                resultado, soma_jogador1, soma_jogador2 = jogar_rodada(mao_jogador1, mao_jogador2)
                print(f"\nResultado da rodada: {resultado} (Jogador 1: {soma_jogador1}, Jogador 2: {soma_jogador2})")

                if resultado.lower() == tipo_aposta.lower():
                    ganho = valor_aposta * (2 if tipo_aposta != "empate" else 8)
                    banca += ganho
                    print(f"\nVocê ganhou! {ganho:.2f} reais.")
                else:
                    print(f"\nVocê perdeu! Perdeu {valor_aposta:.2f} reais.")

                print(f"\nSaldo atual após a rodada: R${banca:.2f}")

                # Reseta a árvore de derivação para a próxima rodada
                arvore_derivacao = None

        except SyntaxError as e:
            print(f"\nErro de sintaxe: {e}")

        if banca <= 0:
            print("\nSua banca acabou. Jogo encerrado!")
            break

if __name__ == "__main__":
    main()