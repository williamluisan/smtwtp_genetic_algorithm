import pandas as pd
import random as rd
import pprint as pp
import helper as h
# import genetic_algorithm as ga
import copy

file_loc = './data/case_1.xls'

# excel data reading, with dict as returned item
def read_excel():
    project = {}
    file = pd.read_excel(file_loc)
    for i, j in file.iterrows():
        if (i != 0):
            project_name = file.iat[i, 1]
            processing_time = int(file.iat[i, 2])
            weight = int(file.iat[i, 3])
            due_date = int(file.iat[i, 4])
            project[project_name] = {
                'p': processing_time, 
                'w': weight,
                'd': due_date
            }
    return project

# convert dictionary to list, for randoming solutions
def convert_dict_to_list():
    project = read_excel()
    
    first_solution = []
    for a in project:
        chromosome = []
        chromosome.append(a)
        chromosome.append(project[a]['p'])
        chromosome.append(project[a]['w'])
        chromosome.append(project[a]['d'])
        for _ in range(4):
            chromosome.append(0)
        first_solution.append(list(chromosome))
    return first_solution


# generate random solutions
first_solution = convert_dict_to_list()
generation = []
for k in range(len(first_solution)):
    rd.shuffle(first_solution)
    generation.append(list(first_solution))

# calculate C, T, wT
gen_calculated = []
for chromosome in generation:
    Ob = 0
    for k, gene in enumerate(chromosome):
        gene[7] = 0
        # completion time
        C = gene[1]
        if (k == 0):
            gene[4] = C
            C_before = C
        else:
            gene[4] = C + C_before
            C_before = gene[4]
    
        # tardiness (T)
        T = gene[3] - gene[4]
        if (T > 0):
            T = 0
        gene[5] = abs(T)

        # weighted tardiness (wT)
        wT = gene[2] * abs(T)
        gene[6] = wT
    
        # fitness function (Ob)
        Ob += wT
    gene[7] = Ob

    # wrap the caluclation of the generation
    gen_calculated.append(copy.deepcopy(chromosome))

print('\n=========')
pp.pprint(gen_calculated)
print('=========')

# new array for sorting
sort_chro = []
for l, chromosome in enumerate(gen_calculated):
    sort_gene = []
    for m, gene in enumerate(chromosome):
        sort_gene.append(gene[0])
        if (m == 5):
            sort_gene.append(gene[7])
    sort_chro.append(list(sort_gene))
    
# sort the sort_chro
sorted_generation = sorted(sort_chro, key=lambda x: x[6])
h.pre(sorted_generation)