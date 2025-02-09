# gramatica.py

GRAMATICA = {
    "COMANDO": [["APOSTA"], ["MAO"], ["ACAO"], ["RESULTADO"]],
    "APOSTA": [["aposta", "TIPO_APOSTA", "VALOR"]],
    "TIPO_APOSTA": [["jogador1"], ["jogador2"], ["empate"]],
    "VALOR": [["NUMERO"]],
    "MAO": [["mao", "CARTA", "CARTA", "CARTA", "CARTA"]],
    "ACAO": [["jogador1", "DECISAO"], ["jogador2", "DECISAO"]],
    "DECISAO": [["manter"], ["pegar"]],
    "CARTA": [["ás"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["10"], ["J"], ["Q"], ["K"]],
    "RESULTADO": [["resultado"]],
}