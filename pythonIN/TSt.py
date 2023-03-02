dados = list()
cadastrados = list()
grand = peque = c = 0
while True:
    c+=1
    print('CADASTRO')
    print('-=-'*6)
    dados.append(str(input('Seu nome: ')))
    dados.append(float(input('Seu peso: ')))

    prox = str(input('Quer continuar? [S/N]')).upper().strip()
    print('-=-'*6)
    if prox == 'N':
        break

    cadastrados.append(dados[:])
    dados.clear()

    for p in cadastrados:
      if c == 1:
        grand = 1
        peque = 1  
      if cadastrados[p] > grand:
         cadastrados[p] = grand    
    
    
     


print(f'O número de cadastrados foram {len(cadastrados)}.')
