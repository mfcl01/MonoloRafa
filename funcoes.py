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

def posicao_valida(dic_navios, linha, coluna, orientacao, tamanho):

    if orientacao == "horizontal" and coluna + tamanho > 10:
        return False
    if orientacao == "vertical" and linha + tamanho > 10:
        return False
    
    nova_posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    for navios in dic_navios.values():
        for posicoes in navios:
            for posicao in posicoes:
                if posicao in nova_posicao:
                    return False
    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto     