from src.process import Process

process = Process()

for i in range(0, 100):
    process.skip_process()

process.inland.inland_population.get_current_iq_distribution(draw=True)

for i in range(0, 10000):
    process.execute_process()

process.inland.inland_population.get_current_iq_distribution(draw=True)
