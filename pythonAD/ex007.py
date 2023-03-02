pessoa1 = {'Nome': 'Miguel Fialho',
    'Gênero': 'Masculino',
    'Ocupação': 'Empreendedor',
    'Planeta Natal': 'Terra'}
print(pessoa1)
pessoa1['Idade'] = 15
print(pessoa1)

encontrado = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}
encontrado['a'] += 1
print('-=-'*9)
for c in encontrado:
    print(c, 'foi encontrado', encontrado[c], 'vez(es)')
print('-=-'*9)
for c in sorted(encontrado):
    print(c, 'foi encontrado', encontrado[c], 'vez(es)')
print('-=-'*9)
for c, v in sorted(encontrado.items()):
    print(c, 'foi encontrado', v, 'vez(es)')    
print('-=-'*9)