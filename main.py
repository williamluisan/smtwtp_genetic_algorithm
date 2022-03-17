
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
data = gnc.convert_dict_to_list(raw_data);
generation = ga.generate_random_solutions(data)

# calculate fitness function
gen_calculated = []
for chromosome in generation:
    chro_calculated = ga.fitness_function(chromosome)

    # wrap the calculation of the generation
    gen_calculated.append(copy.deepcopy(chro_calculated))


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

# print('\n=========')
# pp.pprint(next_generation_candidate)
# print('=========\n')

# mutation process
next_generation_candidate = ga.mutation(next_generation_candidate)

# print('\n=========')
# pp.pprint(next_generation_candidate)
# print('=========\n')
