from src.inland_simulator import InlandSimulator


class Process():

    inland: InlandSimulator = InlandSimulator()
    chosen_top_percentile = 3
    percentage_of_candidates = 0.8
    process_candidates_age = 20

    def skip_process(self):
        self.inland.increase_year()

    def execute_process(self):
        # Retrieve current 20yo population
        candidates = self.inland.get_current_year_population_by_age(
            self.process_candidates_age)

        # Perform selection
        chosen = self.perform_selection(candidates)

        # Remove current chosen from population
        uids = [ind.uid for ind in chosen]
        self.inland.inland_population.remove_individuals(uids)

        # Forward one year
        self.inland.increase_year()

    def perform_selection(self, candidates: []):
        # Sort candidates by iq
        candidates.sort(key=lambda x: x.iq, reverse=True)

        # Pick the top percentile
        number_of_chosen = round(len(candidates) * self.chosen_top_percentile / 100)
        chosen = candidates[0:number_of_chosen]

        return chosen
