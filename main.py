from src.inland_simulator import InlandSimulator

inland_simulator = InlandSimulator()

for i in range(0, 10):
    inland_simulator.increase_year()

print(inland_simulator.inland_population.get_current_iq_distribution(true))
