

print(input.__doc__)
help(input)

def contador(i, f, p=1):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    ;return: sem retorno
    Function created by Miguel Fialho.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c+=p
    print('FIM!')

contador(2, 10)
help(contador)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = somar(3, 2, 5)
r2 = somar(1, 5)
r3 = somar(4)
print(f"Meus calculos deram {r1}, {r2} e {r3}")

def fatorial(num=1):
    f = 1
    for c in range (num , 0, -1):
        f *= c
    return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} e igual {fatorial(n)}.')

def voto(y):
    from datetime import datetime
    idade = datetime.today().year - year
    if idade >= 18 and idade < 65:
        ob = f'Com {idade} anos: VOTO OBRIGATORIO'
        return ob
    elif idade >= 16 and idade <= 17:
        op = f'Com {idade} anos: VOTO OPCIONAL'
        return op
    elif idade >= 65:
        op = f'Com {idade} anos: VOTO OPCIONAL'
        return op
    else:
        ne = f'Com {idade} anos: VOTO NEGADO'
        return ne

print('---'*10)
year = int(input('Em que ano voce nasceu? '))

res = voto(year)
print(res)

def fatorial(num=1, show=False):
    '''-> Calcula o Fatorial de um numero.
       :param num: O numero a ser calculado
       :param show: (opcional) Mostrar ou nao a conta
       :return: O valor de Fatorial de um numero n.
    '''
    if show == False:
        f = 1
        for c in range(num , 0, -1):
            f *= c
        return f
    
    if show == True:
        f = 1
        for c in range(num , 0, -1):
            f *= c
        for co in range(num, 1, -1):
            print(f'{co} x', end=' ')
        print(f'1 = ', end='')
        return f
        
print(fatorial(6, True))

def ficha(nome='<desconhecido>', gols='0'):
    print('---'*10)

    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols.isalpha():
        gols = 0

    tec = f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    return tec

jog = str(input('Nome do jogador: '))
num = str(input('Numero de gols: '))

print(ficha(jog, num))


def leiaInt(st):
    while True:
        num = input(st)
        if num.isnumeric():
            return(num)
        else:
            print('ERRO ! Digite um numero inteiro valido.')


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')

def maior(nums):
    ma = 0
    for i in nums:
        if ma == 0:
            ma = i
            me = i
        if ma < i:
            ma = i
    return ma
    return print(f'O maior valor informado foi {ma}')
def menor(nums):
    me = 0
    for i in nums:
        if me == 0:
            me = i
        if me > i:
            me = i
    if 0 in nums:
        me = 0
    return me

def notas(*nums, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos aluno (aceita várias)
    :param sit: (opcional) indica se dece ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    anly = dict()
    anly['total'] = len(nums)
    anly['maior'] = maior(nums)
    anly['menor'] = menor(nums)
    anly['média'] = sum(nums) / len(nums)
    if sit == True:
        if anly['média'] >= 7:
            anly['situação'] = 'BOA'
        else:
            anly['situação'] = 'RUIM'
    print('---'*10)
    return anly

print(notas(5.5, 9.5, 10, 6.5, 2, 7, sit=True))

from time import sleep
c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[7;30m',    # 3 - branco
     '\033[0;30;44m'  # 4 - azul
     )

def write(txt, cor=0):
    print(c[cor], end='')
    print('~' * (len(txt) + 4))
    print(f'  {txt}  ')
    print('~' * (len(txt) + 4))
    print(c[0], end='')
def ajuda(com):
    write(f"Acessando o manual do comando '{com}'", 4)
    sleep(2)
    print(c[1], end='')
    help(com)
    print(c[0], end='')

def interactive_sys():
    while True:
        
        write('SISTEMA DE AJUDA PyHELP', 2)
        C = input('Função ou Biblioteca > ')
        if C == 'fim':
            write('ATÉ LOGO', 1)
            break 
        ajuda(C)
    
interactive_sys()