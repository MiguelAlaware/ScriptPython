def msg(m):
    print('-' * len(m))
    print(m)
    print('-' * len(m))


def sum(a, b):
    msg('   SUM OF NUMBERS   ')
    print(f'A = {a} e B = {b} ')
    return print(f'a soma de A + B = {a+b}')

def count(*num):
    for valor in num:
        print(f'{valor}', end='')

def double(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1




#Programa principal
sum(124, 256)

count(2, 2, 3)
count(12, 4 , 6)
count(3, 6, 19)

val = [1, 2, 4, 5, 7, 12, 63, 123, 65, 21, 7654, 12, 3124]
double(val)
print(val)

#Desafios

def area(l, c):
    return print(f"A área de um terreno {l}x{c} é de {l*c}m2")    

print('Controle de Terrenos')
print('-'*20)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)

def write(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}  ')
    print('~' * (len(txt) + 4))

write('Miguel Fialho Evangelista')


from time import sleep

def count(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p == 0:
        p = 1 
    if p > 0 and f > i:
        for num in range(i, f+1, p):
            sleep(0.5)
            print(num, end=' ', flush=True)
    elif p < 0 or i > f:
        p = 0 - p
        for num in range(i, f-1, p):
            sleep(0.5)
            print(num, end=' ', flush=True)
    print('FIM!')

print('-=-'*20)
count(1, 10, 1)

print('-=-'*20)
count(10, 0, 2)

print('-=-'*20)
print('Agora é sua vez de personalizar a contagem!')
In = int(input('Início: '))
Fi = int(input('Fim: '))
Pa = int(input('Passo: '))
print('-=-'*20)

count(In, Fi, Pa)

def maior(*nums):
    print('Analisando os valores passados...')
    for vals in nums:
        print(f'{vals}', end=' ')
    print(f'Foram informados {len(nums)} valores ao todo.')
    ma = 0
    for i in nums:
        if ma == 0:
            ma = i
        if ma < i:
            ma = i
    return print(f'O maior valor informado foi {ma}')
        
print('-=-'*20)
maior(2, 9, 4, 5, 7, 1)
print('-=-'*20)
print('-=-'*20)
maior(4, 7, 0)
print('-=-'*20)
print('-=-'*20)
maior(2, 1)
print('-=-'*20)
print('-=-'*20)
maior(6)
print('-=-'*20)
print('-=-'*20)
maior()
print('-=-'*20)

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print("PRONTO!")

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}")

numeros = list()

sorteia(numeros)
somaPar(numeros) 
