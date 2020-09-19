from src.population import Population
from src.individual import Individual
from numpy.random import normal

class InlandSimulator():

    starting_population: int = 10000
    starting_iq_distribution: (int, int) = (100, 15)

    def __init__(self):
        self.year: int = 0
        self.inland_population: Population = Population()

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
        return normal(*self.starting_iq_distribution)
