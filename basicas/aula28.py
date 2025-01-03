"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome: ")
idade = input("digite a sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"seu nome invertido é {nome[::-1]}")
    
    if " " in nome:
        print("seu nome contem espacos")
    else:
        print("seu nome nao contem espacos")
    
    print(f"seu nome contem {len(nome)} letras")
    print(f"a primeira letra do seu nome é: {nome[0]}")
    print(f"a ultima letra do seu nome é: {nome[-1]}")

else:
    print("voce deixou campos vazios")
    