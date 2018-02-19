import random


class Individual:

    ALPHABET = 'abcdefghijklmnopqrstuvxywz '

    def __init__(self, genes):
        self.genes = genes
        self.fitness = None

    def calculate_fitness(self, target):
        score = 0
        for char in range(len(target)):
            if target[char] == self.genes[char]:
                score += 1
        self.fitness = score/len(target)

    def crossover(self, other):
        child_genes = []
        pivot = random.randrange(len(self.genes))
        return Individual(self.genes[:pivot] + other.genes[pivot:])

    def mutate(self, mutation_rate):
        new_genes = list(self.genes)
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                new_genes[i] = random.choice(list(Individual.ALPHABET))
        self.genes = ''.join(new_genes)
