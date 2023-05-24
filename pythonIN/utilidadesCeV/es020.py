try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'problema encontrado foi {erro.__class__}')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados!')
else:
    print(f'O resultado r = {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')
