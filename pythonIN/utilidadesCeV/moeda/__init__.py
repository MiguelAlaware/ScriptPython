def moeda(st):
    return f'R${st}'.replace('.', ',')

def metade(n=0, s=True):
   met = n / 2
   return met if s is False else moeda(met)

def dobro(n=0, s=True):
    doubl = n * 2
    return doubl if s is False else moeda(doubl)

def aumentar(n=0, p=10, s=True):
    up = (n * (p / 100)) + n
    return up if s is False else moeda(up)

def diminuir(n=0, p=10, s=True):
    down = n - (n * (p / 100))
    return down if s is False else moeda(down)


def resumo(val, aum, red):
    print('---'*11)
    print('         RESUMO DO VALOR')
    print('---'*11)
    print(f'Preço analisado:   {moeda(val)}')
    print(f'Dobro do preço:    {dobro(val, True)}')
    print(f'Metade do preço:   {metade(val, True)}')
    print(f'{aum}% de aumento:    {aumentar(val, aum, True)}')
    print(f'{red}% de redução:    {diminuir(val, red, True)}')
    print('---'*11)