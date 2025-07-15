import random


archive = 'archive.txt'
i= random.randint(1, 100)
with open (archive, 'w+') as archive:
    while i < 99:
        archive.write(f'linha {i}\n')
        i = random.randint(1, 100)
    archive.seek(0,0)
    print(archive.read())