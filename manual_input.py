# input projects
import random

total_projects = int(input('Jumlah proyek: '))

chromosom = {}

for i in range(total_projects):
    projects = []
    project_name = input('Nama proyek: ')
    p = int(input(project_name + ' (p) = '))
    w = int(input(project_name + ' (w) = '))
    d = int(input(project_name + ' (d) = '))
    projects.append(p)
    projects.append(w)
    projects.append(d)
    chromosom[project_name] = projects

chromosom = list(chromosom.items())
random.shuffle(chromosom)

print(chromosom)