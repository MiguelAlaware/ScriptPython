
nome = input('Qual é o seu nome?:')
print('Prazer ' + nome + ', meu nome é Fialho')

dia = input('dia que você nasceu:')
mes = input('mês que você nasceu:')
ano = input('ano que você nasceu:')
print('você nasceu no dia', dia, 'do mês de', mes, 'do ano de', ano)
num1 = int(input('primeiro número:'))
num2 = int(input('segundo número:'))
s = num1 + num2
# print('a soma vale', s)
print('A soma entre \n {} e {} vale {}'.format(num1, num2, s))
print(ano.isupper())
print(type(mes))