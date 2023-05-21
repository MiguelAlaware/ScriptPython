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