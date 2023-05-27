try:
    a = int(input('Numerador: '))
    b = int (input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados utilizados digitados.')
except ZeroDivisionError:
    print('Nao e possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados!')
except Exception as erro:
    print(f'Infelizmente tivemos um problema :(, o problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado -> {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!') 
    
def leiaint(integer):
    while True:
        try: 
            intag = int(input(integer))
        except ValueError:
            print('ERRO: por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
            return 0
        else:
            return intag
def leiareal(real):
    while True:
        try: 
            floag = float(input(real))
        except ValueError:
            print('ERRO: por favor, digite um número real válido.')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
            return 0
        else:
            return floag
        
inteiro = leiaint('Digite um Inteiro: ')
real = leiareal('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro')
else:
    print('Tudo Ok!')