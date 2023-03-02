from random import randint


imovel = float(input('Valor do Imóvel: '))
renda = float(input('Sua Renda: '))
parcelamento = int(input('Parcelamento: '))

prestacao = imovel / parcelamento 

if prestacao  >= (0.30 * renda):
    print('Seu empréstimo foi negado!')
else:
    print('empréstimo aprovado!')


print('[1] para conversão Binária')
print('[2] para conversão Hexadecimal')
print('[3] para conversão Octal')
conversao = int(input('[/C]:'))
valor = int(input('Digite um Valor na base Decimal: '))

if conversao == 1:
    print('Na base Binária: {}'.format(bin(valor)))
elif conversao == 2:
    print('Na base Hexadecimal: {} '.format(hex(valor)))
elif conversao == 3:
    print('Na base Octal: {}'.format(oct(valor)))
else:
    print('-=TENTE NOVAMENTE=-')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2, n1))
elif n1 == n2:
    print('não existe um valor maior, os dois são iguais!')

ano = int(input('Ano de nascimento: '))
idade = 2022 - ano
if idade < 18:
    print('Você ainda vai se alistar.')
    print('Falta {} ano(s) no prazo '.format(18 - idade))
elif idade == 18:
    print('Já está na hora de se alistar.')
elif idade > 18:
    print('Já passou o tempo do tempo do alistamento.')
    print('Você passou {} ano(s) do prazo'.format(idade - 18))

print('-='*13)

if idade <= 9:
    print('Atleta de natação MIRIM')
elif 9 < idade <= 14:
    print('Atleta de natação INFANTIL')
elif 14 < idade <= 19:
    print('Atleta de natação JUNIOR')
elif 19 < idade <= 20:
    print('Atleta de natação SÊNIOR')
else:
    print('Atleta de natação MASTER') 


nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
 
media = nota1 + nota2 / 2
if media < 5.0:
    print('Reprovado')
if 5.0 <= media <= 6.9:
    print('Recuperação')
if media > 7.0:
    print('Aprovado')

segm1 = float(input('Medida do Segmento de reta 1: '))
segm2 = float(input('Medida do Segmento de reta 2: '))
segm3 = float(input('Medida do Segmento de reta 3: '))

if segm1 + segm2 > segm3:
    print('Condição de existêcia de um triângulo atendida!')
    if segm1 == segm2 == segm3:
        print('esse é um triângulo equilátero')
    elif segm1 == segm2 or segm1 == segm3 or segm3 == segm2:
        print('esse é um triângulo isósceles')
    elif segm1 != segm2 != segm3:
        print('esse triângulo é Escaleno')
else:
    print('Condição de existência faltante!')

altura = float(input('Digite a sua Altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso / altura ** 2
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < imc <= 25:
    print('Peso ideal')
elif 25 < imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

print('-='*13)

produto = str(input('Digite o produto: '))
preco = float(input('Preço do produto: '))
print('Escolha o método de pagamento: ')
print('-='*13)
print('[1] à vista dinheiro/cheque: 10% desconto.')
print('[2] à vista cartão: 5% desconto.')
print('[3] à 2x no cartão: preço base.')
print('[4] à 3x ou mais no cartão: 20% de juros.')
metodo = int(input('[C/:] '))
if 1 <= metodo <= 4:
    if metodo == 1:
        desconto = preco - (preco * 0.10)
        print('A compra custou R${}'.format(desconto))
    elif metodo == 2:
        desconto = preco - (preco * 0.05)
        print('A compra custou R${}'.format(desconto))
    elif metodo == 3:
        print('A compra custou R${}'.format(preco))
    elif metodo == 4:
        juros = preco + (preco * 0.20)
        print('A compra custou R${}'.format(juros))
else:
    print('-=ERROR=-')

print('-='*13)

print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
jogador = int((input('[C/:] ')))
computador = randint(1, 3)

if 1 <= jogador <= 3:
    print('Jogador jogou {} e o computador jogou {}.'.format(jogador, computador))
    if computador == jogador:
        print('Empate!')
    elif jogador == 1 and computador == 3:
        print('Jogador Venceu!')
    elif jogador == 2 and computador == 1:
        print('Jogador Venceu!')
    elif jogador == 3 and computador == 2:
        print('Jogador Venceu!')
    else:
        print('Jogador Perdeu!')
else:
    print('-=TENTE DENOVO=-')
    
