"""
Interpolação básicas em strings
s - string
d e i - int
f - floar
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preco total foi R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %04X' % (1500, 1500))