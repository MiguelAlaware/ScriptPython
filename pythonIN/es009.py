soma = 0
soma2 = 0

for pr in range(0, 50, 2):
    print(pr)

for im in range(1, 501):
    if im % 3 == 0 and im % 2 == 1:
        soma += im
print(soma)

tabuada = int(input('Digite um número: '))

for tab in range(1, 11):
    mult = tab * tabuada
    print(mult)

inicial = int(input('Número Inicial: '))
final = int(input('Número Final: '))

for som in range(inicial, final+1):
    if som % 2 == 0:
        soma2 += som
print(soma2)

ptermo = int(input('Primeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))

for pa in range (0, 10):
    ptermo += razao
    print(ptermo)

primo = int(input('Digite um número para saber se é primo: '))
for pri in range (2, primo):
    if primo % pri == 0:
        print('Ele não é um número primo! -{}-'.format(pri))
    else:
        print('Ele é um número primo! -{}-'.format(pri))

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ' '.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1 ,-1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')

ma = 0
me = 0

for ano in range(0, 7):
    nascimento = int(input('Digite seu ano de nascimento: '))
    maioridade = 2022 - nascimento
    if maioridade >= 21:
        ma += 1
    elif maioridade < 21:
        me += 1

        
print('{} alcançaram a maioridade e {} não alcançaram a maioridade!'.format(ma, me))

maior = 0
menor = 0

for pe in range (0, 5):
    peso = float(input('Qual o seu peso: '))
    if pe == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

mediaid = 0

for dados in range(0, 4):
    print('-='*13)
    nome = str(input('Seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo: '))
    print('-='*13)

    mediaid += idade
    print('A média de idade dos indivíduos é de {} anos'.format(mediaid / 2))

    