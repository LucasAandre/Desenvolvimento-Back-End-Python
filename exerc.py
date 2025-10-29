'''
Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
'''


numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 

'''
input().split() gera uma lista de strings.

O lambda converte temporariamente cada x em int para testar se é par.

O filter mantém os valores originais (strings) dos pares.

Então, " ".join(pares) junta essas strings filtradas.
'''

'''
A função (no seu caso, a lambda) recebe cada elemento dessa lista um por um.

Se essa função retornar True, o filter() mantém o elemento.

Se retornar False, o filter() descarta o elemento.
'''

# Solução sem filter()
numeros = input("Digite os números separados por espaço: ").split()

pares = []  # lista para guardar os números pares

for numero in numeros:
    if int(numero) % 2 == 0:  # testa se o número é par
        pares.append(numero)  # se for, adiciona à lista

print("Números pares:", " ".join(pares))
