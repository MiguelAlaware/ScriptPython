vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input('digite uma palavra:')
achado = []
for letra in palavra:
    if letra in vogais:
        if letra not in achado:
            achado.append(letra)
for vogal in achado:
    print(vogal)


vogais2 = {'a', 'e', 'i', 'o', 'u'}
palavra2 = input('digite uma palavra:')
achado2 = vogais2.intersection(set(palavra2))
i_lista = sorted(list(achado2))
print(i_lista)

vogais3 = set('aeiou')
palavra3 = input('digite uma palavra:')
achado3 = vogais3.intersection(set(palavra3)) 
for vogal3 in achado3:
    print(vogal3)