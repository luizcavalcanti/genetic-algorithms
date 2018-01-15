# Experimentation with genetic algorithms

## Concepts

**Gene**: The value of a single variable of the problem space solution.

**Genotype**: The collection of genes of an individual. Sometimes called **chromosome** in literature.

**Alphabet**: The solution's variables types. Think of it as the possible values of a gene.

**Fitness**: How 'adequate' a solution is to the given problem. How close or far it is from the optimal or an acceptable solution.

**Fitness function**: An objective function that calculates the fitness of an individual to the problem's solution.

**Population**: Collection of individuals.

**Fenotype**: The visual or functional representation of a genotype.

**Generation**: A group of individuals (population) that is "alive" (active) during a given genetic algorithm iteration.


## Tips

### How to make fitness functions more adequate to my problem?

When the number of variables is too big, an individual with a linear fitness score slightly better than the other tends to be a massively better solution. In those cases, it's recommended to use an exponential way to calculate fitness score, so we can award "small" improvements in the solution space with much more likelihood to generate descendants.

```python
def calculate_fitness(target):
    linear_fitness = ... # some fitness calculation
    return 2 ** linear_fitness
```

### How to improve individual selection for mating?

If the mating pool get too big by inserting the same individuals multiple times to reflect their fitness/chance of survival, we can use [rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling). That method draws a individual from the regular population and tests a probability for keeping it tied to its fitness. If it's rejected, a new individual is drawn from the population. This avoid the creation of a proper mating poll, saving lots of memory, specially in bigger problem spaces, but takes much more cpu time/cycles.


## Examples

* typing_monkeys - N number of monkeys typing randomnly until one of them evolves to type the correct given phrase


