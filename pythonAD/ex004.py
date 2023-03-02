frase = "Don't Panic!"
plista = list(frase)
print(frase)
print(plista)
for i in range(4):
    plista.pop()
plista.pop(0)
plista.remove("'")
plista.extend([plista.pop(), plista.pop()])
plista.insert(2, plista.pop(3))

nova_frase = ''.join(plista)
print(plista)
print(nova_frase)
    
