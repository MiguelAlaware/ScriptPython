from random import randint

vitorias = 0
player = ''

while True:
    machine = ''
    machine2 = randint(0, 10)
    player = str(input('Par ou Ímpar: [P/I]: ')).upper()
    player2 = int(input('Digite um número [0/10]: '))
    
    

    poui = machine2 + player2
    if poui % 2 == 0 and player == 'P':
        print('O player Venceu!!')
    elif poui % 2 == 1 and player == 'I':
        print('o player Venceu')
    else:
        print('O jogador Perdeu! :(')
        break
    vitorias +=1
print(f'Vitórias consecutivas: {vitorias}')

print('-=-'*3)
print('CADASTRO')
print('-=-'*6)

cont1 = cont2 = cont3 = 0
continuar = sexo = ''

while True: 
    idade = int(input('Digite sua Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite seu sexo [M/F]:')).upper()
    print('-=-'*6)
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar [S/N]: ')).upper()
    if idade > 18:
        cont1+=1
    if sexo == 'M':
        cont2+=1
    if sexo == 'F' and idade < 20:
        cont3+=1
    if continuar == 'N':
        break
print(f'Pessoas +18: {cont1}')
print(f'Homens cadastrados: {cont2}')
print(f'Mulheres com -20: {cont3}')

cont = total = mil = maiorp = menorp = 0
produtob = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: '))
    cont+=1
    parar = str(input('Quer continuar? [S/N]: ')).upper()
    total+=preco
    if preco > 1000:
        mil+=1

    if cont == 1:
        maiorp = preco
        produtob = produto
    if preco > maiorp:
        maiorp = preco
    if preco < maiorp:
        menorp = preco
        produtob = produto
    if parar == 'N':
        break
print(f'O total gasto foi R${total}.')
print(f'{mil} produto(s) custa(m) mais que R$1000.')
print(f'O produto mais barato é {produtob} por apenas {menorp}')


valor = int(input('Digite o valor no qual você que sacar: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

