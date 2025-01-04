"""
Iterando string com while
"""
#       012345678910
# nome = 'Luiz Otávio' #Iteraveis
#     -1110987654321


nome = 'Maria Helena'

contador = 0
nome_iterado = ''
while contador < len(nome):
    
    letra = nome[contador]
    nome_iterado += f'*{letra}'
    
    contador += 1

nome_iterado += '*'
print(nome_iterado)