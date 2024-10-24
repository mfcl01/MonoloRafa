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