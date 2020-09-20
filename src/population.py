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

    def get_current_iq_distribution(self, draw: bool):
        iqs = {}
        for uid in self.individuals:
            rounded_iq = round(self.individuals[uid].iq)
            if rounded_iq in iqs:
                iqs[rounded_iq] += 1
            else:
                iqs[rounded_iq] = 1

        if draw:
            plt.plot(iqs)
            plt.ylabel("IQ")
            plt.show()
        return iqs
