
import pprint as pp
import helper as h
import genetic_algorithm
import generic
import copy

# class instance
ga = genetic_algorithm.Genetic_algorithm();
gnc = generic.Generic();

# generate random solutions
raw_data = gnc.read_excel();
# print('\n=========')
# pp.pprint(raw_data)
# print('=========\n')

data = gnc.convert_dict_to_list(raw_data);
generation = ga.generate_random_solutions(data)
# print('\n=========')
# pp.pprint(generation)
# print('=========\n')


# calculate fitness function
gen_calculated = []
for chromosome in generation:
    chro_calculated = ga.fitness_function(chromosome)

    # wrap the calculation of the generation
    gen_calculated.append(copy.deepcopy(chro_calculated))

# print('\n=========')
# pp.pprint(gen_calculated)
# print('=========\n')

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

print('\n=========')
pp.pprint(sorted_generation)
print('=========\n')

# store the minimum Ob founded
minimum_Ob = sorted_generation[0][6]
# pp.pprint(minimum_Ob)

# selection and crossover process for making a new generation
next_generation_candidate = ga.selection(sorted_generation)

# print('\n=========')
# pp.pprint(next_generation_candidate)
# print('=========\n')

# mutation process
next_generation = ga.mutation(next_generation_candidate)

print('\n=========')
pp.pprint(next_generation)
print('=========\n')

# get gene data
gene_data_list = []
new_chromosome_list = []
for chromosome in next_generation:
    gene_data_list = []
    for gene in chromosome:
        # h.pre(raw_data[gene])
        gene_data = [gene, raw_data[gene]['p'], raw_data[gene]['w'], raw_data[gene]['d'], 0 , 0 , 0, 0]
        gene_data_list.append(gene_data)
    new_chromosome_list.append(gene_data_list)

# calculate fitness function
gen_calculated2 = []
for chromosome in new_chromosome_list:
    chro_calculated = ga.fitness_function(chromosome)

    # wrap the calculation of the generation
    gen_calculated2.append(copy.deepcopy(chro_calculated))

# create new array for chromosome and total weighted tardiness
sort_chro = []
for l, chromosome in enumerate(gen_calculated2):
    sort_gene = []
    for m, gene in enumerate(chromosome):
        sort_gene.append(gene[0])
        if (m == 5):
            sort_gene.append(gene[7])
    sort_chro.append(list(sort_gene))

# sort the sort_chro
sorted_generation = sorted(sort_chro, key=lambda x: x[6])

print('\n=========')
pp.pprint(sorted_generation)
print('=========\n')