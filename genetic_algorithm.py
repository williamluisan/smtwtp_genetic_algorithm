import random as rd
import pprint as pp
import helper as h
from collections import Counter

# generate random solutions from excel data


def generate_random_solutions(data):
    # generate random solutions
    generation = []
    for k in range(len(data)):
        rd.shuffle(data)
        generation.append(list(data))
    return generation


# fitness function
"""
    for the fitness function will be calculating
    C = Processing time
    T = Tardiness
    wT = Weighted Tardiness
    and Ob as Total Weighted Tardiness
"""


def fitness_function(chromosome):
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
    return chromosome

# selection


def selection(sorted_generation):
    next_gen = []
    sorted_generation_len = len(sorted_generation) - 1

    print('\n=========')
    pp.pprint(sorted_generation)
    print('=========')

    # select the 2 of the best chromosome as next gen candidate
    next_gen.append(sorted_generation[0])
    next_gen.append(sorted_generation[1])

    for k, chromosome in enumerate(sorted_generation):
        # popping out Ob value from chromosome
        chromosome.pop()

    # print('\n=========')
    # pp.pprint(sorted_generation)
    # print('=========')

    # need to make sure how many times to do crossover
    for _ in range(2):
        # pick random number
        rand_numb_1 = rd.randint(2, sorted_generation_len)
        rand_numb_2 = rd.randint(2, sorted_generation_len)
        while(rand_numb_1 == rand_numb_2):
            rand_numb_2 = rd.randint(2, sorted_generation_len)

        # do crossover chromosome
        new_chro_a, new_chro_b = crossover(
            sorted_generation[rand_numb_1], sorted_generation[rand_numb_2]
        )

        next_gen.append(new_chro_a)
        next_gen.append(new_chro_b)

    return next_gen


# crossover
def crossover(chro_a, chro_b):
    a = chro_a[4:]
    b = chro_b[4:]

    a_new = chro_a[0:4] + b
    b_new = chro_b[0:4] + a

    # h.pren(a_new)
    # h.pren(b_new)

    return a_new, b_new

# mutation
def mutation(generation):
    # check if there's same project inside a chromosome
    new_gen = []

    for k, chromosome in enumerate(generation):
        for l, gene in enumerate(chromosome):
            if gene in chromosome:
                
            else:
                continue