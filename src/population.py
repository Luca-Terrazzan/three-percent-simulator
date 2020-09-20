from src.individual import Individual


class Population():

    def __init__(self):
        self.individuals = {}

    def add_individual(self, individual: Individual):
        self.individuals[individual.uid] = individual

    def remove_individuals(self, uids):
        for uid in uids:
            del self.individuals[uid]
