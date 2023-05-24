from uteis import numeros

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} = {fat}")
print(f"O dobro de {num} = {numeros.dobro(num)}")
print(f"O triplo de {num} = {numeros.triplo(num)}")

from utilidadesCeV import moeda, dado

p = dado.leiaDinheiro('Digite o preco: R$')
moeda.resumo(p, 80, 35)