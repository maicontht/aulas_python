"""
Faça um alista de compras com listas
o usuário deve ter a possibilidade de 
inseir, apagar e listar valores da sua lista
Nao permita que o programa quebre com 
erros de indices inexistentes na lista.
"""
"""

========================MINHA VERSAO DE RESOLUCAO==============================
import os
lista_compras = []

while True:
    comando = input(f'Selecione a opção \
\n[i]nserir [a]pagar [l]istar: ').lower()

    if comando == 'i':
        os.system('cls')
        add_lista = input('Valor: ')
        lista_compras.append(add_lista)
        os.system('cls')

    elif comando == 'a':
        os.system('cls')
        exc_lista= input('Escolha o índice para apagar: ')
        try:
            exc_lista_int = int(exc_lista)
            del lista_compras[exc_lista_int]
            os.system('cls')
        except:
            os.system('cls')
            print('Digite um indice valido')
        
    elif comando == 'l':
        os.system('cls')
        if lista_compras == []:
            print('Nada para listar')
        for indice, item in enumerate(lista_compras):
            print(indice, item)
    
    else:
        print('Digite i, a ou l')
================================================================================
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')