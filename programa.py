import funcoes
frota_inicial = [ 
    {'nome': 'porta-aviões','tamanho': 4, 'quantidade': 1 },
    {'nome': 'navio-tanque','tamanho': 3, 'quantidade': 2 },
    {'nome': 'contratorpedeiro','tamanho': 2, 'quantidade': 3 },
    {'nome': 'submarino','tamanho': 1, 'quantidade': 4 }, 
    ]

frota = {}

for navio in frota_inicial:
    nome = navio['nome']
    tamanho = navio['tamanho']
    quantidade = navio['quantidade']
    for i in range(quantidade):
        while True:
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
            linha = int(input('Digite a linha: '))
            coluna = int(input('Digite a coluna: '))
            orientacao = None

            if nome != 'submarino':
                orientacao = int(input('Digite 1 para a posição vertical ou 2 para a posição horizontal horizontal: '))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'

            if funcoes.posicao_valida(frota, linha, coluna, orientacao, tamanho):
                funcoes.preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break
            else:
                print('Esta posição não está válida!')

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = funcoes.posiciona_frota(frota_oponente)
tabuleiro_jogador = funcoes.posiciona_frota(frota)
jogando = True
já_atacados = []
        
while jogando == True:
    tabuleiros = funcoes.monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(tabuleiros)
    i = 0
    while i == 0:
        linha = int(input('Digite a linha que deseja atacar: '))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Digite a linha que deseja atacar: '))      
        coluna = int(input('Digite a coluna que deseja atacar: '))
        while coluna < 0 or coluna > 9:    
            print ('Coluna inválida!')
            coluna = int(input('Digite a coluna que deseja atacar: '))
        if [linha, coluna] not in já_atacados:
            já_atacados.append([linha,coluna])
            i = 1
        else:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
          
    tabuleiro_oponente = funcoes.faz_jogada(tabuleiro_oponente, linha, coluna)
    total_afundados = funcoes.afundados(frota_oponente, tabuleiro_oponente)

    if total_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
        






