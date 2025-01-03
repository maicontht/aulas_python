numero_str = input('vou dobrar o numero que voce digitar: ')

if numero_str.isdigit():
    numero_float = float (numero_str)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso nao é um numero')
    