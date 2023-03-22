def check_fermat(a, b, c, n):
    prep = a**n + b**n 
    if n == 2 and prep == c**n:
        print("Holy smokes Fermat was wrong!")
    else:
        print('No, that does not work')
def giv(a, b, c, n):
    a = int(input("Valor de a: "))
    b = int(input("Valor de b: "))
    c = int(input("Valor de c: "))
    n = int(input("valor de n: "))
    check_fermat(a, b, c, n)

def is_triangle(n, m, w):
    if n + m < w:
        print('No')
    elif n + w < m:
        print('No')
    elif m + w < n:
        print('No')
    else:
        print('Yes')
def giv2():
   lista = list()
   for c in range(0, 3):
       lista.append(int(input('Digite o comprimento de um lado: ')))
   is_triangle(lista[0], lista[1], lista[2]) 

def recurse(nn, s):
    """ This function is basically a sequencie that its rate is going to increase 1 by 1 and adding... *the args cannot be a negative number* """
    if nn == 0:
        print(s)
    else:
        recurse(nn-1, nn+s)

recurse(5, 0)