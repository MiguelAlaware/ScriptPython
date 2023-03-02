
carro = {}
digito = input("Digite o modelo de um carro:")
if digito not in carro:
    carro[digito] = 0
else:
    carro[digito] += 1
for m, f in carro.items():
    print("O modelo de carro {} apareceu {} vez(es)".format(m, f))

fruta = {}
digita = str(input("digite a sua fruta predileta:"))
fruta.setdefault(digita, 0)
fruta[digita] +=1

for f, q in fruta.items():
    print("A sua fruta predileta é {}, ({}). ".format(f, q))

    

