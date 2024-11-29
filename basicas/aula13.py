nome = 'Maicon Gomes'
altura = 1.70
peso = 80
imc = peso / (altura * altura)

#f-strings
linha_1 =  f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Maicon Gomes tem 1.70 de altura,
# pesa 80 quilos e seu IMC É
# 27.68166089965398 