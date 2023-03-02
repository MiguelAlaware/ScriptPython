vogais = {'a', 'e', 'e', 'i', 'o', 'u', 'u'}
vogais2 = set('aeiou')
print( vogais, vogais2)
palavra = "ola"
u = vogais.union(set(palavra))
u_lista = sorted(list(u))
print(u_lista)
d = vogais.difference(set(palavra))
d_lista = sorted(list(d))
print(d_lista)
i = vogais.intersection(set(palavra))
i_lista = sorted(list(i))
print(i_lista)
