# sintatico.py

from gramatica import GRAMATICA

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    def __str__(self, level=0):
        ret = "  " * level + f"{self.value}\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.comando()

    def comando(self):
        if self.pos >= len(self.tokens):
            raise SyntaxError("Fim inesperado da entrada")
        
        token = self.tokens[self.pos]
        if token == "aposta":
            return self.aposta()
        elif token == "mao":
            return self.mao()
        elif token == "resultado":
            return self.resultado()
        else:
            raise SyntaxError(f"Token inesperado: {token}")

    def aposta(self):
        self.pos += 1  # Consome 'aposta'
        tipo_aposta = self.tipo_aposta()
        valor = self.valor()
        return Node("aposta", [tipo_aposta, valor])

    def tipo_aposta(self):
        if self.pos >= len(self.tokens):
            raise SyntaxError("Fim inesperado da entrada")
        
        token = self.tokens[self.pos]
        if token in ["jogador", "banqueiro", "empate"]:
            self.pos += 1
            return Node("tipo_aposta", [Node(token)])
        else:
            raise SyntaxError(f"Tipo de aposta inválido: {token}")

    def valor(self):
        if self.pos >= len(self.tokens):
            raise SyntaxError("Fim inesperado da entrada")
        
        token = self.tokens[self.pos]
        if token.isdigit():
            self.pos += 1
            return Node("valor", [Node(token)])
        else:
            raise SyntaxError(f"Valor inválido: {token}")

    def mao(self):
        self.pos += 1  # Consome 'mao'
        carta1 = self.carta()
        carta2 = self.carta()
        return Node("mao", [carta1, carta2])

    def carta(self):
        if self.pos >= len(self.tokens):
            raise SyntaxError("Fim inesperado da entrada")
        
        token = self.tokens[self.pos]
        if token in ["ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]:
            self.pos += 1
            return Node("carta", [Node(token)])
        else:
            raise SyntaxError(f"Carta inválida: {token}")

    def resultado(self):
        self.pos += 1  # Consome 'resultado'
        return Node("resultado")