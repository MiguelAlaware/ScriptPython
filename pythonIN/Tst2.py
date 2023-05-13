jogadores = list()
jogador = dict()
continuar = 'S'

while continuar == 'S':
    
    jogador['Nome'] = str(input('Nome do Jogador: '))
    jogador['gols'] = []
    jogador['total'] = 0
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    for g in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {g+1}? ')))
        jogador['total'] += jogador['gols'][g]
    jogadores.append(jogador.copy())
    jogador.clear()

    continuar = str(input('Quer continuar [S/N]: ')).upper()
    print('-=-'*20)

print('cod ', end='')
for i in jogadores[0].keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('---'*20)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Nao existe jogador com codigo {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols.')
    print('---'*20)
print('<<<VOLTE SEMPRE>>>')