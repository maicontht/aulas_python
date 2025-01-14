"""
Faça um alista de compras com listas
o usuário deve ter a possibilidade de 
inseir, apagar e listar valores da sua lista
Nao permita que o programa quebre com 
erros de indices inexistentes na lista.
"""
import os
lista_compras = []

while True:
    comando = input(f'Selecione a opção \
\n[i]nserir [a]pagar [l]istar: ').lower()

    if comando == 'i':
        os.system('cls')
        add_lista = input('Valor: ')
        lista_compras.append(add_lista)

    if comando == 'a':
        exc_lista= input('Escolha o índice para apagar: ')
        exc_lista_int = int(exc_lista)
        del lista_compras[exc_lista_int]
        
    if comando == 'l':
        for indice, item in enumerate(lista_compras):
            print(indice, item)