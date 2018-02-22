load 'population.rb'
load 'individual.rb'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz '
TARGET = 'to be or not to be'
DNA_SIZE = TARGET.size
INDIVIDUALS_COUNT = 100
MUTATION_RATIO = 0.01

# create initial population
pop = Population.new(DNA_SIZE, ALPHABET, INDIVIDUALS_COUNT)

# run fitness for population
pop.calculate_fitness(TARGET)
pop.print_population_info

# while no individual reaches threshold fitness
until pop.reached_solution do
  # generate new population
  pop.new_generation(MUTATION_RATIO)
  # calculate fitness
  pop.calculate_fitness(TARGET)
  pop.print_population_info
end
