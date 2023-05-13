from random import randint
from time import sleep
from operator import itemgetter
nom = str(input('Nome: '))
med = float(input(f'Media de {nom}: '))
bolet = {'Nome': nom, 'Media': med}
print(f'O nome e igual a {bolet["Nome"]}')
print(f'A media e igual a {bolet["Media"]}')
if bolet['Media'] > 7.0:
    print('Situacap atual e igual a Aprovado')
else:
    print('Situacao atual e igual a Reprovado')

players = dict()
sorting = list()
rolls_nums = list()
c = 1
mai = men = 0
print('Valores Sorteados')
for plays in range(4):
    players['P'+ str(c)]= randint(1, 6)  
    c+=1
for v in players.values():
    rolls_nums.append(v)
for keys, values in players.items():
    print(f'{keys} tirou o numero {values}')
    sleep(1)
print('Ranking dos jogadores')
sorting = sorted(players.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(sorting):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = 2023 - nasc
pessoa['CPTS'] = int(input('Carteira de trabalho (0 nao tem): '))
if pessoa['CPTS'] != 0:
    pessoa['Empregado'] = int(input('Ano de contratacao: '))
    pessoa['Salario'] = int(input('Salario: '))
    pessoa['Aposentadoria'] = pessoa['Empregado'] + 35 - nasc
print('-=-'*10)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

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

pessoas = list()
dictemp = dict()
mulh = list()
med = 0
while True:
    print('=-=-=-LEITOR DE PESSOAS-=-=-=')
    dictemp['Nome'] = str(input('Nome: '))
    dictemp['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    dictemp['Idade'] = int(input('Idade: '))
    med += dictemp['Idade']

    pessoas.append(dictemp.copy())
    dictemp.clear()

    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
    else:
        continue

print('-=-'*20)
print(f"A) O Grupo tem {len(pessoas)} pessoas.")

med = med/len(pessoas)
print(f'B) A média de idade é de {med}.')

for i in range(len(pessoas)):
    if pessoas[i]['Sexo'] == 'F':
        mulh.append(pessoas[i]['Nome'])
print(f'C) As mulheres cadastradas foram: {mulh}')

print(f'D) Lista das pessoas que estão acima da média: ')
for p in range(len(pessoas)):
    if pessoas[p]['Idade'] > med:
        print(f"nome = {pessoas[p]['Nome']}; sexo = {pessoas[p]['Sexo']}; idade = {pessoas[p]['Idade']};")
        print()
print("<< ENCERRADO >>")

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