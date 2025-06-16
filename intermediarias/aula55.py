# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
# MEU JEITO

cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
state =  ['BA', 'SP', 'MG', 'RJ']

def zipper(list1, list2):
    temp = ()
    city_state = []
    i = 0
    for city in cities:
        
        temp = city, state[i]
        city_state.append(temp)
        i += 1
    return city_state
    
result = zipper(cities, state)

print(result)
print(result[0])
print(result[1])
print(result[2])

