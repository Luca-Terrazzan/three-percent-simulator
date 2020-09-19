from population import Population
from individual import Individual
from numpy.random import normal

class InlandSimulator():

    starting_population = 10000
    starting_iq_distribution = (100, 15)

    def __init__(self):
        self.year = 0
        self.inland_population = Population()

        self.create_starting_population()

    def create_starting_population(self) -> None:
        for i in range(0, self.starting_population):
            ind = Individual(
                uid=i,
                yob=self.year,
                iq=self.get_random_iq_from_current_distribution()
            )
            self.inland_population.add_individual(ind)

    def get_random_iq_from_current_distribution(self) -> int:
        return normal(self.starting_iq_distribution)
