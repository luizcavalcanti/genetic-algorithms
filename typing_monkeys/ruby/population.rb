class Population
  def initialize(dna_size, alphabet, individuals_count)
    @dna_size = dna_size
    @alphabet = alphabet
    @individuals_count = individuals_count
    @generations = 1
    generate_initial_population
  end

  def calculate_fitness(target)
    @individuals.each do |ind|
      ind.calculate_fitness(target)
    end
    @individuals = @individuals.sort_by { |k| k.fitness }.reverse
  end

  def print_population_info
    puts "generation #{@generations}"
    puts "================"
    @individuals.first(20).each do |ind|
      puts "#{'%.5f' % ind.fitness} - #{ind.genes.join('')}"
    end
  end

  def reached_solution
    @individuals.first.fitness == 1.0
  end

  def new_generation(mutation_rate)
    new_generation = []
    mating_pool = []

    @individuals.each do |ind|
      mating_pool += Array.new((ind.fitness * 100).floor, ind)
    end

    (0..@individuals_count-1).each do |i|
      a = (rand * mating_pool.size).floor
      b = (rand * mating_pool.size).floor

      parent_a = mating_pool[a]
      parent_b = mating_pool[b]

      child = parent_a.crossover(parent_b)
      child.mutate(mutation_rate)

      new_generation << child
    end
    @generations += 1
    @individuals = new_generation
  end

  private

  def generate_initial_population
    @individuals = []
    (0..@individuals_count-1).each do |i|
      genes = []
      (0..@dna_size-1).each do |gene|
        genes[gene] = @alphabet[(rand * @alphabet.size).floor]
      end
      @individuals << Individual.new(genes, @alphabet)
    end
  end
end
