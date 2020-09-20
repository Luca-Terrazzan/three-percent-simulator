from src.inland_simulator import InlandSimulator

inland_simulator = InlandSimulator()

for i in range(0, 1000):
    inland_simulator.increase_year()

# print(inland_simulator.inland_population.get_current_iq_distribution(True))
print(inland_simulator.inland_population.get_current_age_distribution(1000, True))
