


vogais = ["a", "e", "i", "o", "u"]
palavra = input("Digite uma palavra aqui:")
achado = []
for letra in palavra:
    if letra in vogais:
        if letra not in achado:
            achado.append(letra)
for vogais in achado:
    print(vogais)

