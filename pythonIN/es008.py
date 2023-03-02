from time import sleep
s = 0


inicio =  int(input('Digite o Início: '))
fim = int(input('Digite o Fim: '))
passo = int(input('Digite o Passo: '))
for c in range(inicio, fim+1, passo):
    print(c)
print('-FIM-')

for p in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('O somatório de todos os valores foi {}'.format(s))

for cr in range(10, 0, -1 ):
    sleep(1)
    print(cr)
print('Feliz Ano Novo!!!!')
