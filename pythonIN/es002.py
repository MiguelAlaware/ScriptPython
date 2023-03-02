tipos = input('Digite algo para saber seu tipo e características:')
print('Tipo primitivo:', type(tipos))
print('Letras capitalizadas:', tipos.isupper())
print("Variável numérica:", tipos.isnumeric())

num1 = int(input('digite um numero para ver algumas operações:'))
print('Sucessor:{} \nAntecessor:{}'.format(num1+1, num1-1))
print('Dobro:{}\nTriplo:{}\nRaiz quadrada:{}'.format(num1*2, num1*3, num1**0.5))

nota1 = float(input('Digite a primeita nota:'))
nota2 = float(input('Digite a segunda nota:'))
x = (nota1 + nota2) / 2
print('A média aritmética entre suas notas é {}'.format(x))

