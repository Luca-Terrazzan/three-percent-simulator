import matplotlib.pyplot as plt
from src.individual import Individual


class Population():

    def __init__(self):
        self.individuals = {}

    def add_individual(self, individual: Individual):
        self.individuals[individual.uid] = individual

    def remove_individuals(self, uids):
        for uid in uids:
            del self.individuals[uid]

    def get_individuals_by_year(self, year: int):
        individuals = []
        for uid in self.individuals:
            if self.individuals[uid].yob == year:
                individuals.append(self.individuals[uid])

        return individuals

    def get_current_iq_distribution(self, draw: bool):
        iqs = {}
        for uid in self.individuals:
            rounded_iq = round(self.individuals[uid].iq)
            if rounded_iq in iqs:
                iqs[rounded_iq] += 1
            else:
                iqs[rounded_iq] = 1

        if draw:
            self.draw_distribution(iqs)

        return iqs

    def get_current_age_distribution(self, current_year: int, draw: bool):
        ages = {}
        for uid in self.individuals:
            age = current_year - self.individuals[uid].yob
            if age in ages:
                ages[age] += 1
            else:
                ages[age] = 1

        if draw:
            self.draw_distribution(ages)

        return ages

    def draw_distribution(self, distribution):
        lists = sorted(distribution.items())  # sorted by key, list of tuples
        x, y = zip(*lists)  # unpack a list of pairs into two tuples
        plt.plot(x, y)
        plt.show()
