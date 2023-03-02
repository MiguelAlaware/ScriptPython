def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('Olá', 4)
print('-'*20)

def print_na(obje, nume):
    if nume <= 0:
        return
    print(obje)
    print_na(obje, nume-1)
    

print_na(print_n('Hello', 1), 4)