frase = "Don't panic!"
plista = list(frase)
print(frase)
print(plista)

nova_lista = ''.join(plista[1:3])

nova_lista = nova_lista + "".join([plista[5], plista[4], plista[7], plista[6]])

print(plista)
print(nova_lista)
