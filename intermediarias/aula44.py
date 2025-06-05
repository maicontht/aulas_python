import importlib

import aula44_m

print(aula44_m.variavel)

for i in range(10):
    importlib.reload(aula44_m)
    print(i)

print('Fim')