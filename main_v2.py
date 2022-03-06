from concurrent.futures import process
import pandas as pd
import random as rd
import pprint as pp
import helper as h

file_loc = 'C:/Users/Lunba7th/Code/thesis/data/case_1.xls'

project = []

# excel data reading
file = pd.read_excel(file_loc)
for i, j in file.iterrows():
    if i != 0:
        project_name = file.iat[i, 1]
        processing_time = int(file.iat[i, 2])
        weight = int(file.iat[i, 3])
        due_date = int(file.iat[i, 4])
        values = [project_name, processing_time, weight, due_date, 0, 0, 0]
        project.append(values)

# generate random solution
generation = {}
for a in range(len(project)):
    generation[a] = ''
    rd.shuffle(project)
    generation[a] = list(project)

# h.pren(generation)

# calculate C, T, wT
for b in range(len(generation)):
    for c in range(len(generation[b])):
        generation[b][1][4] = generation[b][1][1]

h.pre(generation)


