paranoid_android = "Marvin"
letras = list(paranoid_android)
for letra in letras:
    print('\t', letra)

paranoid_androidS =  "Marvin, the Paranoid Android"
letrasS = list(paranoid_androidS)
for letraS in letrasS[:6]:
    print('\t', letraS)
print()
for letraS in letrasS[-7:]:
    print('\t'*2, letraS)
for letraS in letrasS[12:20]:
    print('\t'*3, letraS)
