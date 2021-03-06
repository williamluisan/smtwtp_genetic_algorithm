import itertools
import pprint as pp
import helper as h
import genetic_algorithm
import generic
import copy
from itertools import permutations

# class instance
ga = genetic_algorithm.Genetic_algorithm();
gnc = generic.Generic();

if __name__ == "__main__":
    # default total tardiness (TT)
    TT = 999999999999
    best_solution = ''
    counter_stop = 0
    flag_stop = 0
    x = 0
    while flag_stop != 1:
        # first random solution
        if x == 0:
            # generate random solutions, get data from excel (data/case_1.xls)
            raw_data = gnc.read_excel();
            data = gnc.convert_dict_to_list(raw_data);
            generation = ga.generate_random_solutions(data)
            
            x += 1
        else:
            # get gene data
            gene_data_list = []
            new_chromosome_list = []
            for chromosome in next_generation:
                gene_data_list = []
                for gene in chromosome:
                    gene_data = [gene, raw_data[gene]['p'], raw_data[gene]['w'], raw_data[gene]['d'], 0 , 0 , 0, 0]
                    gene_data_list.append(gene_data)
                new_chromosome_list.append(gene_data_list)
                generation = new_chromosome_list

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

        """ uncomment line 63 if you want to see all the generated solutions"""
        # h.pren(sorted_generation)

        # store the minimum Ob founded
        if sorted_generation[0][6] < TT:
            TT = sorted_generation[0][6]
            best_solution = sorted_generation[0]
        
        if TT == TT:
            counter_stop += 1
        else:
            counter_stop = 0
            
        if counter_stop == 100:
            h.pren(best_solution)
            h.pren(TT)
            flag_stop = 1

        # selection and crossover process for making a new generation
        next_generation_candidate = ga.selection(sorted_generation)

        # mutation process
        next_generation = ga.mutation(next_generation_candidate)