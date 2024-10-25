def define_posicoes(linha, coluna, orientacao, tamanho):
    t = 1

    coord_inicial = [linha, coluna]
    lista_resultado = [coord_inicial]

    if orientacao == "vertical":
        while t < tamanho:
            lista_resultado.append([linha + t, coluna])
            t += 1

    elif orientacao == "horizontal":
        while t < tamanho:
            lista_resultado.append([linha, coluna + t])
            t += 1
    
    return lista_resultado

def preenche_frota (frota, nome_do_navio, linha, coluna, orientacao, tamanho ):

    define_posicoes
    if nome_do_navio not in frota.keys():
        frota[nome_do_navio] = []
    frota[nome_do_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))


    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(frota):
    grid = []
    v = 0
    while v < 10:
        add = [0] * 10 
        grid.append(add)
        v += 1
    
    for todos_barcos in frota.values():
        for barcos in todos_barcos:
            for coord in barcos:
                line = coord[0]
                column = coord[1]
                grid[line][column] = 1
    return grid

def afundados(frota, tabuleiro):
    sinked = 0 
    for todos_barcos in frota.values():
        for barcos in todos_barcos:
            x = 0
            for coord in barcos:
                line = coord[0]
                column = coord[1]
                if tabuleiro[line][column] == "X":
                    x += 1
            if x == len(barcos):
                sinked += 1 
    return sinked 
