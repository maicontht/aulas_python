# Exercicios com fuções

# Crie uma função que multiplica todos os argumentos
# Não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor
# da variavel

# Crie uma função fala se um numero é par ou impar.
# Retorne se o numero é par ou impar

def multip(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
mult_final = multip(1,2,3,4,5)
print(mult_final)

###############################################################

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'



print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))
