jogador = dict()
jogador['Nome'] = str(input('Nome do Jogador: '))
jogador['gols'] = []
jogador['total'] = 0

partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for g in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {g}? ')))
    jogador['total'] += jogador['gols'][g]

print('-=-'*15)
print(jogador)
print('-=-'*15)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-'*15)

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for p in range(len(jogador['gols'])):
    print(f"   => Na partida {p}, fez {jogador['gols'][p]} gols.")
print(f'Foi um total de {jogador["total"]}')