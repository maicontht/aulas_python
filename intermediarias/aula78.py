# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
# MY SOLUTION
import os

tasks = []
save_tasks = []

while True:
    print('Comandos: listar, desfazer, refazer\n')
    command = input('Digite uma tarefa ou comando ').lower()
    os.system('cls')

    if command == 'listar':
        if not tasks:
            print('Tarefas está vazia!\n')
            
        else:
            print(tasks)
            print(save_tasks)

    elif command == 'desfazer':
        
        if not tasks:
            print('Não da pra desfazer uma lista vazia 🙁\n')
        else:
            tasks.pop()

    elif command == 'refazer':
        if not save_tasks:
            print('Não é possivel refazer sem valores anteriores 🤨\n')

        elif len(save_tasks) > 0:
            last = save_tasks.pop()
            tasks.append(last)
         
    else:
        tasks.append(command)
        save_tasks.append(command)



