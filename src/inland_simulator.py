from random import random
from numpy.random import normal

from src.population import Population
from src.individual import Individual


class InlandSimulator():

    starting_population: int = 10000
    starting_iq_distribution: (int, int) = (100, 15)

    def __init__(self):
        self.year: int = 0
        self.inland_population: Population = Population()

        self.create_starting_population()

    def create_starting_population(self) -> None:
        for i in range(0, self.starting_population):
            ind = self.generate_individual(i)
            self.inland_population.add_individual(ind)

    def get_random_iq_from_current_distribution(self) -> int:
        return normal(*self.starting_iq_distribution)

    def increase_year(self):
        # Increase year counter
        self.year += 1

        # Determine who dies
        individuals_to_remove = []
        for uid in self.inland_population.individuals:
            if self.is_dying(self.inland_population.individuals[uid]):
                individuals_to_remove.append(uid)
        self.inland_population.remove_individuals(individuals_to_remove)
        current_population_size = len(self.inland_population.individuals)

        # Add newborns
        # Newborns are the same amount as deaths
        for i in range(0, self.starting_population - current_population_size):
            newborn = self.generate_individual(i)
            self.inland_population.add_individual(newborn)

    # TODO: upgrade with gompertz distribution instead of linear
    # TODO: precalculate death chances instead of at every step
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gompertz.html
    def is_dying(self, individual: Individual) -> bool:
        age = self.year - individual.yob
        if age <= 20:
            return False
        chance_to_die = (age - 20) / 100
        roll = random()
        return roll < chance_to_die

    def generate_individual(self, number: int) -> Individual:
        return Individual(
            uid=self.generate_uid(number),
            yob=self.year,
            iq=self.get_random_iq_from_current_distribution()
        )

    def generate_uid(self, number) -> str:
        return f'{self.year}_{number}'

    def get_current_year_population_by_age(self, age: int):
        return self.inland_population.get_individuals_by_year(self.year - age)
