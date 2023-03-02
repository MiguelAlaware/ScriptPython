from random import randint

pessoa = ('Miguel', 15, 'M', 68)
del(pessoa)
print(pessoa)

numero_extenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']


numero = int(input('Digite um número para ler por extenso: '))
while numero > 20 or numero < 0:
    numero = int(input('Tente novamente, digite um número para ler por extenso: '))

print(numero_extenso[numero])


serie_a = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude' )

print(f'''Primeiros 5 colocados:
-----
 [1] -> {serie_a[0]}
-----
 [2] -> {serie_a[1]}
----- 
 [3] -> {serie_a[2]}
----- 
 [4] -> {serie_a[3]}
-----
 [5] -> {serie_a[4]}
----- 

''')

print(f'''Últimos 4 colocados:
-----
 [20] -> {serie_a[-1]}
-----
 [19] -> {serie_a[-2]}
----- 
 [18] -> {serie_a[-3]}
----- 
 [17] -> {serie_a[-4]}
-----

''')

print(f'O Goiás está na posição {serie_a.index("Goiás") + 1}')



maior = menor = cont = 0

numero_aleatorios = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999) )

for contagem in range(0, 5):
    
    cont+=1
    numeros_listados = numero_aleatorios[contagem]
    
    
    if cont == 1:
        maior = menor = numeros_listados
    else:
        if numeros_listados > maior:
            maior = numeros_listados
        if numeros_listados < menor:
            menor = numeros_listados

print(f'''Os números listados foram: {numero_aleatorios} ''')
print(f'O maior número foi: {maior}')
print(f'O menor número foi: {menor}')
print(sorted(numero_aleatorios))


v1 = v2 = v3 = v4 = 0
for contagem in range(4):
    valores = int(input('Digite um número: '))
    if v1 == 0:
        v1 = valores
    elif v2 == 0:
        v2 = valores
    elif v3 == 0:
        v3 = valores
    elif v4 == 0:
        v4 = valores

    tupla = (v1, v2, v3, v4)
    


print(f'Quantas vezes que apareceu 9: {list(tupla).count(9)}')
if 3 in tupla:
    print(f'Em que posição apareceu o primeiro 3: {tupla.index(3)}')
else:
    print(f'O número 3 não aparece na tupla')
print('Os números pares foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end='')
print(tupla)


print('-'*20)
print('      LISTAGEM')
print('-'*20)
cont = 0
cont2 = 0
produtos_preco = ('Alvejante', 45, 'Pão', 12, 'Caderno', 25, 'Caneta', 10, 'Camisa', 100, 'Suco', 8, 'Tênis', 500, 'Bola', 89)
quant = len(produtos_preco)
for contagem in range(quant):
    
    cont+=1
    print(f'{produtos_preco[contagem+cont2]}.......R${produtos_preco[contagem+cont]}')
    cont2+=1
    

palavras = ('Carro', 'Caixa', 'Automovel', 'Rua', 'Ataque', 'Ortaliça')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos -> ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
