import os

def exibir_nome_programa():
    print('''
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

    print()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('clear')
    print('Finalizando o programa\n')

def escolher_opcao():
    opcao_escolhida = int(input('\nEscolha uma opção: '))

    print()

    if opcao_escolhida == 1:
        print('Cadastrar restauante')

    elif opcao_escolhida == 2:
        print('Listar restaurantes')

    elif opcao_escolhida == 3:
        print('Ativar restaurantes')

    else:
        finalizar_app()

    '''
    Existe a opção math (Switch Case do C++):

    opcao_escolhida = int(input('Escolha uma opção: '))

    match opcao_escolhida:
    
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida!')
    '''

def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

'''
A variável __name__ não é sempre igual a '__main__', mas ela assume esse valor em situações específicas.

Em resumo:

__name__ == '__main__': Isso acontece quando o arquivo Python é executado diretamente. Ou seja, você roda 
o script usando python nome_do_arquivo.py. Nesse caso, o Python define a variável __name__ como '__main__'.
__name__ == 'nome_do_módulo': Quando um arquivo Python é importado como um módulo em outro arquivo, a 
variável __name__ recebe o nome do módulo (que geralmente é o nome do arquivo sem a extensão .py).
Analogia:

Imagine que você tem uma receita de bolo (arquivo_receita.py).

Executando diretamente: Se você decidir fazer o bolo seguindo essa receita diretamente (python arquivo_receita.py), 
então, para a receita, ela é a "principal" (__main__).
Importando a receita: Se você tem um livro de receitas (meu_livro_de_receitas.py) e usa um trecho da receita do bolo
 (import arquivo_receita), então a receita do bolo é apenas um "módulo" dentro do seu livro, e o nome dela é arquivo_receita.
No contexto da aula, a condição if __name__ == '__main__': é usada para garantir que a função main() seja executada
 apenas quando o script é o programa principal, e não quando é importado como um módulo em outro lugar.
'''
