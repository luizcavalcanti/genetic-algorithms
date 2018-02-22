class Individual
  attr_accessor :genes
  attr_accessor :fitness

  def initialize(genes, alphabet)
    @genes = genes
    @alphabet = alphabet
  end

  def calculate_fitness(target)
    score = 0
    @genes.each_with_index do |gene, index|
      score = score + 1 if target[index]==gene
    end
    @fitness = score/Float(@genes.size)
  end

  def crossover(other)
    pivot = (rand * (@genes.size-2)).floor
    Individual.new(@genes[0..pivot] + other.genes[(pivot+1)..(@genes.size-1)], @alphabet)
  end

  def mutate(ratio)
    (0..@genes.size-1).each do |i|
      @genes[i] = @alphabet[(rand * @alphabet.size).floor] if rand < ratio
    end
  end
end
