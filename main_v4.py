from collections import Counter
import pandas as pd
import random as rd
import pprint as pp
import helper as h
import copy

file_loc = './data/case_1.xls'

# excel data reading
project = []
file = pd.read_excel(file_loc)
for i, j in file.iterrows():
    if (i != 0):
        project_name = file.iat[i, 1]
        processing_time = int(file.iat[i, 2])
        weight = int(file.iat[i, 3])
        due_date = int(file.iat[i, 4])
        values = [project_name, [processing_time, weight, due_date, 0, 0, 0, 0]]
        project.append(list(values))

# generate random solutions
chromosome = project
generation = []
for k in range(len(chromosome)):
    rd.shuffle(chromosome)
    generation.append(list(chromosome))

# calculate C, T, wT
gen_calculated = []
for chromosome in generation:
    Ob = 0
    for k, gene in enumerate(chromosome):
        gene[1][6] = 0
        if (k == 0):
            # completion time (C)
            C = gene[1][0]
            gene[1][3] = C
            C_before = C
        else:
            # completion time (C)
            C = gene[1][0]
            gene[1][3] = C + C_before
            C_before = gene[1][3]
        
        # tardiness (T)
        T = gene[1][2] - gene[1][3]
        if (T > 0):
            T = 0
        gene[1][4] = abs(T)

        # weighted tardiness (wT)
        wT = gene[1][1] * abs(T)
        gene[1][5] = wT

        # fitness function (Ob)
        Ob += wT
    gene[1][6] = Ob

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
            sort_gene.append(gene[1][6])
    sort_chro.append(list(sort_gene))
    
# sort the sort_chro
sorted_generation = sorted(sort_chro, key=lambda x: x[6])
h.pre(sorted_generation)