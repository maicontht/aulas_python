# copy, sorted, produtos.sortAdd 
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Outra possivel solução para copiar lista e alterar valor (list comprehension)

# updated_produtos = [
                        
#     {**produto, 'preco': produto['preco'] * 1.10}
#     for produto in produtos 
# ]

updated_produtos= copy.deepcopy(produtos)

for item in updated_produtos:
    item['preco'] *= 1.10

ordened_produtos_aumentados = sorted(updated_produtos, key=lambda x: x['nome'], reverse= True)

ordened_produtos_aumentados_price = sorted(updated_produtos, key=lambda x: x['preco'])

print(*ordened_produtos_aumentados, sep= '\n')
print(*ordened_produtos_aumentados_price, sep= '\n')
