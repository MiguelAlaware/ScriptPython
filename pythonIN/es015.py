galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai+=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen+=1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

dados = list()
cadastrados = list()
grand = peque = c = 0
i = 1
while True:
    print('CADASTRO')
    print('-=-'*6)
    dados.append(str(input('Seu nome: ')))
    dados.append(float(input('Seu peso: ')))
    prox = str(input('Quer continuar? [S/N]')).upper().strip()
    print('-=-'*6)
    
    cadastrados.append(dados[:])
    dados.clear()

    for p in range(i):
      if c == 0:
        grand = 1
        peque = 1 
      if cadastrados[c][1] > grand:
        grand = cadastrados[c][1]
        peque = cadastrados[c][1]
      if cadastrados[c][1] < peque:
        peque = cadastrados[c][1]
      c+=1  
      
    if prox == 'N':
        break

conjt_num = [[], []]
conta = 0

for val in range(0, 7):
    conta+=1
    esp = int(input(f'Digite seu {conta}' + 'o. ' + 'valor: ')) 
    if esp % 2 == 0:
      conjt_num[0].append(esp)
    else:
       conjt_num[1].append(esp)



print(f'Os números ímpares foram: {sorted(conjt_num[0])}')
print(f'Os números pares foram: {sorted(conjt_num[1])}')
     
matriz = [[],
          [],
          []]
i = 1
j = 1
pos = pares = mai = men = 0
for elem in range(0, 9):
    val = int(input(f'Digite um valor para [{i}, {j}] --> '))
    matriz[pos].append(val)
    
    if pos == 1:
        mai = val
        men = val
        if val > mai:
            mai = val
        if val < men:
            men = val
    
    if len(matriz[pos]) == 3:
        pos+=1
    
    if val % 2 == 0:
        pares+=val

    i+=1
    if i == 4:
        j+=1
        i-=3

print('-=-'*20)
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]\n[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]\n[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
print('-=-'*20)

print(f'A soma dos valores da terceira coluna iguala a: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')

print(f'A soma dos valores pares iguala a: {pares}')

print(f'O maior valor da segunda linha foi: {mai}')

from random import randint
from time import sleep 

print('-'*30)
print('      JOGA NA MEGA SENA          ')
print('-'*30)
quant = int(input('Quantos jogos para sortear? '))

lista = list()
jogos = list()

tot = 1

while tot <= quant:
     cont = 0
     while True:
      num = randint(0, 60)
      if num not in lista:
          cont+=1
          lista.append(num)
      if cont >= 6:
          break
     lista.sort()
     jogos.append(lista[:])
     lista.clear()
     tot+=1
for i, l in enumerate(jogos):
   sleep(2)
   print(f'Jogo {i}: {l}')


boletim = []
rel = []
while True:
     aluno = str(input('Nome do Aluno: '))
     n1 = float(input('Primeira nota: '))
     n2 = float(input('Segunda nota: '))
     rel.append(aluno)
     rel.append(n1)
     rel.append(n2)
     boletim.append(rel[:])
     rel.clear()
     prox = str(input('Quer continuar? [S/N]: ')).upper().strip()
     
     if prox == 'N':
          break

for u, r in enumerate(boletim):
     print('-='*10)
     print(f'Aluno -{u}-')
     print(f'Nome: {r[0]}')
     print(f'Nota(1): {r[1]}')
     print(f'Nota(2): {r[2]}')
     avg = (r[1] + r[2]) / 2
     print(f'Media: {avg}')
     print('-='*10)
while True:
     see = int(input('>> Mostrar notas de qual aluno? (999 interrompe): '))
     if see == 999:
          break
     print(f'Notas de {boletim[see][0]} sao [{boletim[see][1]}, {boletim[see][2]}]')
