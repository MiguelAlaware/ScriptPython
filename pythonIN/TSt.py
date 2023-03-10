from random import randint
from time import sleep  
jogos = []

quant = int(input('Quantidade de jogos para sorteio: '))
print('-=-'*10)
count = posit = 0
while count != quant:
     count+=1
     randomizer = [randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60)]
     
     jogos.append(randomizer)

     print(f'jogo {count}: {jogos[posit]}')
     sleep(2)
     posit+=1
print('-=-'*10)
