from src.inland_simulator import InlandSimulator

inland_simulator = InlandSimulator()

for i in range(0, 100):
    inland_simulator.increase_year()

print(inland_simulator)
