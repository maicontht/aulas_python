# nos caminhos de sys.path

import aula43_m
from aula43_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(aula43_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula43_m.soma(2, 3))