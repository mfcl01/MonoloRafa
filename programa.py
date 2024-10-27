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
print(frota)






