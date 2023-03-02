from random import randint  


n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    n1 = int(input('número: '))
    r = str(input('Quer continuar? [S/N]')).upper()

n2 = 1
par = impar = 0
while n2 != 0:
    n2 = int(input('Digite um valor: '))
    if n2 != 0:
        if n2 % 2 == 0:
            par += 1
        else:
            impar += 1
print('-> Números pares: {}'.format(par))
print('-> Números ímpares: {}'.format(impar))


sexo = str(input('Qual o seu sexo [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite um dado válido [M/F]: ')).upper()


contador1 = 1
pc = randint(0, 10)
jogador = int(input('Digite um número de 0 a 10: '))
while jogador != pc:
    jogador = int(input('Digite um número de 0 a 10: '))
    contador1 += 1
else:
    print('Você acertou o número, foram necessárias {} tentativas!'.format(contador1))



menu = 0
while menu != 5:
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    m = valor1 * valor2
    s = valor1 + valor2
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    menu = int(input('[C/:] -> '))
    if menu == 1:
        print('[A soma vale {}] '.format(s))
    if menu == 2:
        print('[A multiplicação vale {}] '.format(m))
    if menu == 3:
        if valor1 == valor2:
            print('[Os números possuem o mesmo valor] ')
        elif valor1 > valor2:
            print('[O {} é maior que {}] '.format(valor1, valor2))
        elif valor2 > valor1:
            print('[O {} é maior que {}] '.format(valor2, valor1))


fatorial = 1
contador2 = 0
num = int(input('Digite um número: '))
while contador2 != num:
    contador2 += 1 
    fatorial = fatorial * contador2
    print(fatorial)

ni = int(input('Digite um número inicial: '))
r = int(input('Digite um número razão: '))
c1 = 0
t = 0
m = 10
PA = ni 
while m != 0:
    t = t + m
    while c1 != t:
        c1 +=1
        PA += r
        print('Termo({}) = [{}]'.format(c1, PA))
    m = int(input('Quantos termos adicionais: '))


numero_elementos = int(input('Quantos elementos você quer mostrar: '))
cont = 1
primeiro_termo = 0
segundo_termo = 1
print('{} -> {}'.format(primeiro_termo, segundo_termo), end='')
while cont != numero_elementos:
    terceiro_termo = primeiro_termo + segundo_termo
    cont+=1
    primeiro_termo=segundo_termo
    segundo_termo=terceiro_termo
    print(' -> {}'.format(terceiro_termo), end='')
    

parada = 0
total = 0
while parada != 999:
    numero = int(input('Digite um número inteiro: '))
    print('-='*15)
    parada = numero
    total+=numero
print(total-999)


resposta = 'S'
menorv = 0
maiorv = 0
elementos = 0
valor = 0

while resposta == 'S':
    elementos+=1
    digitenum = int(input('número: '))
    resposta = str(input('Quer continuar? [S/N] -> ')).upper()
    valor+=digitenum
    media = valor/elementos
    
    
    if elementos == 1:
        maiorv = menorv = digitenum
    else:
        if digitenum > maiorv:
            maiorv = digitenum
        if digitenum < menorv:
            menorv = digitenum

print('A média dos valores é {}'.format(media))
print('Maior número: {}'.format(maiorv))
print('Menor número: {}'.format(menorv))

