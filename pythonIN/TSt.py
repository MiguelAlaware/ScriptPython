from es020a.lib.interface import *
from es020a.lib.arquivo import *
from time import sleep

arq = 'cadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('\033[033mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[031mERRO! Digite uma opção válida!\033[m')
        sleep(2)