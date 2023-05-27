def leiaint(integer):
    while True:
        try: 
            intag = int(input(integer))
        except ValueError:
            print('\033[031mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[031mO usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return intag
        
def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[033m{c}\033[033m - \033[034m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[032mSua Opção: \033[m')
    return opc