from time import sleep
from random import randint
from random import shuffle

import math




print('Programas Matemáticos')
print('-='*13)
sleep(1)
num = float(input('primeiro número de utilização: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A parte inteira de {} é {}'.format(num, math.floor(num)))

print('-='*13)
sleep(1)
co = float(input('Cateto Oposto: ')) 
ca = float(input('Cateto Adjacente: '))
print('O valor da hipotenusa é  igual a {}'.format(math.hypot(co, ca)))

print('-='*13)
sleep(1)

angulo = math.radians(float(input('digite um valor de um ângulo: ')))

if 0 < math.degrees(angulo) < 360: 
    print('Seno: {}, Cosseno: {}, Tangente: {}'.format(math.sin(angulo), math.cos(angulo), math.tan(angulo)))
else:
    print('coloque um valor menor que 360 e maior que 0!')

print('-='*13)
sleep(1)

alunos = ['Brian', 'Rodinei', 'Clodovil', 'Chaco']
aleatorio = randint(0, 3)
print('O aluno escolhido para apagar o quadro foi: {}'.format(alunos[aleatorio]))

print('-='*13)
sleep(1)
shuffle(alunos)
print('Ordem de apresentação: {} '.format(alunos))

