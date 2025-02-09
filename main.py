# main.py

from lexico import tokenizar
from sintatico import Parser, Node
from jogo import jogar_rodada, gerar_mao
import os

def registrar_arvore_derivacao(arvore):
    if not os.path.exists("registros"):
        os.makedirs("registros")
    with open("registros/log_arvoreDerivacao.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(str(arvore) + "\n\n")

def main():
    banca = 1000.00

    while True:
        print(f"\nSaldo atual: R${banca:.2f}")
        if banca <= 0:
            print("\nSua banca acabou. Jogo encerrado!")
            break

        entrada = input("Digite um comando (ex: 'aposta jogador 100', 'mao', 'resultado'): ")
        tokens = tokenizar(entrada)

        try:
            parser = Parser(tokens)
            arvore = parser.parse()
            print("\nÁrvore de Derivação:")
            print(arvore)
            registrar_arvore_derivacao(arvore)

            if tokens[0] == "aposta":
                tipo_aposta = tokens[1]
                valor_aposta = float(tokens[2])
                if valor_aposta > banca:
                    print("\nVocê não tem dinheiro suficiente para essa aposta.")
                    continue

                banca -= valor_aposta
                mao_jogador = gerar_mao()
                mao_banqueiro = gerar_mao()

                print("\nMão do jogador:", mao_jogador)
                print("Mão do banqueiro:", mao_banqueiro)

                resultado, soma_jogador, soma_banqueiro = jogar_rodada(mao_jogador, mao_banqueiro)
                print(f"\nResultado da rodada: {resultado} (Jogador: {soma_jogador}, Banqueiro: {soma_banqueiro})")

                if resultado.lower() == tipo_aposta.lower():
                    ganho = valor_aposta * (2 if tipo_aposta != "empate" else 8)
                    banca += ganho
                    print(f"\nVocê ganhou! {ganho:.2f} reais.")
                else:
                    print(f"\nVocê perdeu! Perdeu {valor_aposta:.2f} reais.")

                print(f"\nSaldo atual após a rodada: R${banca:.2f}")

        except SyntaxError as e:
            print(f"\nErro de sintaxe: {e}")

        if banca <= 0:
            print("\nSua banca acabou. Jogo encerrado!")
            break

if __name__ == "__main__":
    main()