from collections import Counter
import pandas as pd
import random as rd
import pprint as pp
import helper as h
import copy

file_loc = './data/case_1.xls'

project = []

# excel data reading
file = pd.read_excel(file_loc)
for i, j in file.iterrows():
    if (i != 0):
        project_name = file.iat[i, 1]
        processing_time = int(file.iat[i, 2])
        weight = int(file.iat[i, 3])
        due_date = int(file.iat[i, 4])
        values = [project_name, [processing_time, weight, due_date, 0, 0, 0]]
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
    for k, gene in enumerate(chromosome):
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

    # wrap the caluclation of the generation
    gen_calculated.append(copy.deepcopy(chromosome))

print('\n=========')
pp.pprint(gen_calculated)