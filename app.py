import os

restaurantes = ['Bella Sushi', 'Don Corleone']

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
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurantes()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        
        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    
    except:
        opcao_invalida()
    
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


def opcao_invalida():
    print('\nOpção inválida! Digite apenas números de 1 a 4.\n')
    voltar_menu_principal()


def cadastrar_restaurantes():
    titulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()


def listar_restaurantes():
    titulo('Lista de Restaurantes')
    
    for i, restaurante in enumerate(restaurantes, start=1):
        print(f'{i}. {restaurante}')

    voltar_menu_principal()


def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def titulo(string):
    os.system('clear')
    print(string)
    print()


def main():
    os.system('clear')
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
