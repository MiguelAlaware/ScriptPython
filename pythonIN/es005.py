import random

player = int(input('Digite um número: '))
computador = random.randint(0, 5)
if player == computador:
    print('Você VENCEU!')
else:
    print('GAME OVER!')

motorista = float(input('Digite a kilometragem média: '))
if motorista > 80:
    multa = (motorista - 80) * 7
    print('Você foi multado!')
    print('Sua multa é de R${}'.format(multa))
else:
    print('Continue no seu caminho')

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('Esse número é par')
else:
    print('Esse número é ímpar')

viagem = float(input('Qual a distância de sua viagem? '))
if viagem <= 200:
    preco = viagem * 0.50
    print('Sua viagem custou R${}'.format(preco))
else:
    preco = viagem * 0.45
    print('Sua viagem custou R${}'.format(preco))

salario = float(input('Digite aqui o seu salário: '))
if salario > 1250:
    aumento = (salario * 0.10) + salario
    print('Seu salário é agora de {}'.format(aumento))
else:
    aumento = (salario * 0.15) + salario
    print('Seu salário é agora de {}'.format(aumento))