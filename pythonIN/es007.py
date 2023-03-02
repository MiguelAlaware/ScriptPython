nome = str(input('Digite seu nome completo: '))
print('-='*1)
print('Seu nome Maiúsculo: {}'.format(nome.upper()))
print('Seu nome Minúsculo: {}'.format(nome.lower()))
contar = len(nome.strip())
print('Letras ao todo: {}'.format(contar))
dividir = nome.split()
print('Letras no primeiro nome: {}'.format(len(dividir[0])))
print('Silva no nome: {} '.format('Silva' in nome))
print('Primeiro nome: {}'.format(dividir[0]))
print('Último nome: {}'.format(dividir[len(nome)-1]))

print('-='*13)

numero = int(input('Digite um número:(0 a 9999) '))
n = str(numero)
if 0 <= numero <= 9999: 
    print('Unidade: {}'.format(n[3]))
    print('Dezena: {}'.format(n[2]))
    print('Centenas: {}'.format(n[1]))
    print('Milhar: {}'.format(n[0]))

print('-='*13)

cidade = str(input('Diga o nome de uma cidade: ')).split()
print('Santo' in cidade[0])

print('-='*13)

frase = str(input('Digite uma frase: ')).lower()
contador = frase.count('a')
achadorp = frase.find('a')
achadoru = frase.find('a')
print('A letra -a- aparece {} vez(es) na frase apresentada'.format())
print('primeira posição: {}'.format(achadorp) + 1)
print('última posição: {}'.format(achadoru) + 1)



