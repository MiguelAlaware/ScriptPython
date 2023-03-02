mediaid = 0

menorida = 0
maiorida = 0

countmu = 0
nomestg = ''

for dados in range(0, 4):
    print('-='*13)
    nome = str(input('Seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo: ')).lower()
   
    mediaid += idade
    if sexo == 'masculino':
        if dados == 1:
            menorida = idade
            maiorida = idade
            nomestg = nome
        else:
            if idade > maiorida:
                maiorida = idade
                nomestg = nome
            if idade < menorida:
                menorida = idade
    if sexo == 'feminino' and idade < 20:
        countmu += 1
print('O nome do homem mais velho é {}'.format(nomestg))
print('A média de idade dos indivíduos é de {} anos'.format(mediaid / 2))
print('{} tem menos de 20 anos'.format(countmu))