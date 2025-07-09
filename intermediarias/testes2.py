caminho_arquivo = 'aula116.txt'


v1 = 'Ola mundo cruel'
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')
    arquivo.write(v1)