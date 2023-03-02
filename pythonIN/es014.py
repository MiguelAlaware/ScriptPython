num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Número não encontrado')
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(4)
valores.append(3)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Lista Finalizada')

value = list()
for cont in range(0, 5):
    value.append(int(input('Digite um valor:')))

a = [2, 3, 4, 7]
b = a[:]

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

lista = []
for val in range(5):
   lista.append(int(input(f'Digite um valor({val}):  ')))  
   if val == 0:
    maiorq = menorq = lista[val]
   else:
    if lista[val] > maiorq:
        maiorq = lista[val]
    if lista[val] < menorq:
        menorq = lista[val]

listadc = []
while True:
    valu_num = int(input('Digite algum valor: '))
    if valu_num in listadc:
        print('Número Duplicado Tente novamente!')
        listadc.remove(valu_num)
    listadc.append(valu_num)
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

listadc.sort()
print(f'A lista obtida foi --> {listadc}')

   

print(f'O maior número foi {maiorq} na posição ', end='')
for i, v in enumerate(lista):
    if v == maiorq:
        print(f'{i}...', end='')
print()
print(f'O menor número foi {menorq} na posição ', end='')
for i, v in enumerate(lista):
    if v == menorq:
        print(f'{i}...', end='')
print()


listaN = []
for con in range(0, 5):
    nrb = int(input('Digite um valor: '))
    if con == 0 or nrb > listaN[len(listaN)-1]:
        listaN.append(nrb)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(listaN):
            if nrb <= listaN[pos]:
                listaN.insert(pos, nrb)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {listaN}')

quantosn = 0
malista = []
while True:
    numbr = int(input('Digite um valor: '))
    nex = str(input('Quer continuar[S/N] -> ')).upper()
    malista.append(numbr)
    quantosn+=1
    if nex == 'N':
        break

malista.sort(reverse=True)
print(f'Foram digitados {quantosn} números!')
print(f'A sua lista na ordem descrescente {malista}')
if 5 in malista:
    print(' ---> O número 5 está presente na lista')
else:
    print(' ---> O número 5 não está presente na lista')


par = []
impar = []
total = []
while True:
    dign = int(input('Digite um valor: '))
    total.append(dign)

    if dign % 2 == 0:
        par.append(dign)
    elif dign % 2 == 1:
        impar.append(dign)

    contin = str(input('Quer continuar [S/N] --> ')).upper()
    if contin == 'N':
        break

print(f'A lista de valores total foi: {total}')
print(f'A lista de números pares foi: {par}')
print(f'A lista de números ímpares foi {impar}')

contador = 0
expression = str(input('Digite uma expressão matemática: '))
verification = list(expression)

if '(' in verification and ')' not in verification:
    print('A expressão está errada')
elif ')' in verification and '(' not in verification:
    print('A expressão está errada')

for i in verification:
    if i == '(' or i == ')':
        contador+=1
if contador % 2 == 1:
    print('A expressão está errada')
else:
    print('Sua expressão é válida!')
