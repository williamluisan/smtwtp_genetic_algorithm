import pandas as pd
import pprint as pp
import helper as h
import genetic_algorithm as ga
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

    data = []
    for a in project:
        chromosome = []
        chromosome.append(a)
        chromosome.append(project[a]['p'])
        chromosome.append(project[a]['w'])
        chromosome.append(project[a]['d'])
        for _ in range(4):
            chromosome.append(0)
        data.append(list(chromosome))
    return data


# generate random solutions
data = convert_dict_to_list()
generation = ga.generate_random_solutions(data)

# calculate fitness function
gen_calculated = []
for chromosome in generation:
    chro_calculated = ga.fitness_function(chromosome)

    # wrap the caluclation of the generation
    gen_calculated.append(copy.deepcopy(chro_calculated))

# print('\n=========')
# pp.pprint(gen_calculated)
# print('=========')

# create new array for chromosome and total weighted tardiness
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

# store the minimum Ob founded
minimum_Ob = sorted_generation[0][6]
pp.pprint(minimum_Ob)

# selection and crossover process for making a new generation
next_generation_candidate = ga.selection(sorted_generation)

print('\n=========')
pp.pprint(next_generation_candidate)
print('=========\n')

next_generation_candidate = ga.mutation(next_generation_candidate)
