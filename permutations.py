import pandas as pd
from itertools import permutations
import helper as h
import generic
import genetic_algorithm as ga
import copy

gene = generic.Generic()
ga = ga.Genetic_algorithm()

if __name__ == "__main__":
    data_excel = gene.read_excel()
    main_data = ['A', 'B', 'C', 'D', 'E', 'F']
    main_data = list(permutations(main_data))
    
    generation = []
    for chromosome in main_data:
        data = []
        chromosome = list(chromosome)
        for gene in chromosome:
            new_chromosome = []
            new_chromosome.append(gene)
            new_chromosome.append(data_excel[gene]['p'])
            new_chromosome.append(data_excel[gene]['w'])
            new_chromosome.append(data_excel[gene]['d'])
            for _ in range(4):
                new_chromosome.append(0)
            data.append(list(new_chromosome))
        generation.append(data)
    
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
    h.pren(sorted_generation[0])