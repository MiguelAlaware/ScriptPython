vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input('Digite uma palavra para saber as vogais e sua frequência:')
encontrado = {'a': 0, 'i': 0, 'e': 0, 'o': 0, 'u':0}

for letra in palavra:
    if letra in vogais:
        print(letra)
        encontrado[letra] += 1

for c, v in sorted(encontrado.items()):
    print(c, 'foi encontrado', v, 'vez(es)')
