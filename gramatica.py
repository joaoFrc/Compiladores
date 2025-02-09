# gramatica.py

GRAMATICA = {
    "COMANDO": [["APOSTA"], ["MAO"], ["RESULTADO"]],
    "APOSTA": [["aposta", "TIPO_APOSTA", "VALOR"]],
    "TIPO_APOSTA": [["jogador"], ["banqueiro"], ["empate"]],
    "VALOR": [["NUMERO"]],
    "MAO": [["mao", "CARTA", "CARTA"]],
    "CARTA": [["ás"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["10"], ["J"], ["Q"], ["K"]],
    "RESULTADO": [["resultado"]],
}