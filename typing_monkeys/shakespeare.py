from population import Population

import matplotlib.pyplot as plt

avg_fitness = []
best_fitness = []
generations = []

def print_population_stats(population):
    print("="*30)
    print("Generation: %d" % population.generations)
    print("Best fitness: %f" % population.best_fitness())
    print("Average fitness: %f" % population.average_fitness())
    print("\n".join([x.genes for x in population.current_generation[:20]]))

def plot_data(population):
    generations.append(population.generations)
    avg_fitness.append(population.average_fitness())
    best_fitness.append(population.best_fitness())
    plt.plot(generations, best_fitness, 'r')
    plt.plot(generations, avg_fitness, 'b')
    plt.pause(0.001)


target = "to be or not to be"
#target = "a arte existe porque a vida nao basta"

population_size = 200
mutation_rate = 0.01
gene_size = len(target)

fig=plt.figure()
plt.axis([0, 500, 0, 1])
plt.ion()
# plt.show()

pop = Population(population_size, gene_size)
pop.calculate_fitness(target)
print_population_stats(pop)
plot_data(pop)

while not pop.reached_solution(target):
    pop.select_survivors()
    pop.spawn_new_generation(mutation_rate)
    pop.calculate_fitness(target)
    print_population_stats(pop)
    plot_data(pop)

input("done.")
