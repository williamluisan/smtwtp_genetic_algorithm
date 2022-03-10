def generate_random_solutions()
    # generate random solutions
    generation = []
    for k in range(len(first_solution)):
        rd.shuffle(first_solution)
        generation.append(list(first_solution))