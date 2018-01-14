from individual import Individual

import math
import random

class Population:

    ALPHABET = 'abcdefghijklmnopqrstuvxywz '

    def __init__(self, population_size, gene_size):
        self.current_generation = []
        self.generations = 1

        for i in range(population_size):
            genes = ''.join([random.choice(Population.ALPHABET) for n in range(gene_size)])
            self.current_generation.append(Individual(genes))

    def calculate_fitness(self, target):
        for individual in self.current_generation:
            individual.calculate_fitness(target)
        self.current_generation.sort(key=lambda x: x.fitness, reverse=True)

    def select_survivors(self):
        self.mating_pool = []
        for i in self.current_generation:
            n = int(i.fitness * 100)
            for j in range(n):
                self.mating_pool.append(i)

    def spawn_new_generation(self, mutation_rate):
        new_generation = []
        pool_size = len(self.mating_pool)
        for i in range(len(self.current_generation)):
            a = random.randrange(pool_size)
            b = random.randrange(pool_size)
            parent_a = self.mating_pool[a]
            parent_b = self.mating_pool[b]
            child = parent_a.crossover(parent_b)
            child.mutate(mutation_rate)
            new_generation.append(child)
        self.current_generation = new_generation
        self.generations += 1

    def reached_solution(self, target):
        for i in self.current_generation:
            if i.genes == target:
                return True
        return False

    def best_fitness(self):
        return self.current_generation[0].fitness

    def average_fitness(self):
        total = 0.0
        for i in self.current_generation:
            total += i.fitness
        return total/len(self.current_generation)
