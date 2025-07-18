import json

teste4 = produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def dumpar_json():
    with open('teste4.json', 'w', encoding='utf8')  as archive:
        json.dump(teste4, archive, indent= 2)

def loadar_json():
    with open('teste4.json', 'r', encoding='utf8') as archive:
        teste = json.load(archive)
        print(teste)

print(dumpar_json())
print(loadar_json())