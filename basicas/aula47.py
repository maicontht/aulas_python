"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'Maa'
ocultar_palavra = len(palavra_secreta) * '*'
contagem_tentativas = 0

while True:
    tentativa_palavra = input('Digite uma letra: ').lower()


    if type(tentativa_palavra) != str: 
        print('Digite apenas letras')

    elif len(tentativa_palavra) > 1:
        print('Digite apenas uma letra')

    contagem_tentativas += 1