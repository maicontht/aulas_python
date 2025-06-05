from sys import path
# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

import aula46_package.modulo
from aula46_package import modulo
from aula46_package.modulo import *
# import aula99_package.modulo
# from aula99_package import modulo
# from aula99_package.modulo import *

# from aula99_package.modulo import soma_do_modulo
# # from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula46_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# from aula46_package.modulo import fala_oi, soma_do_modulo

# print(__name__)
# fala_oi()

from aula46_package import soma_do_modulo, falar_oi

print(soma_do_modulo(2, 3))
falar_oi()