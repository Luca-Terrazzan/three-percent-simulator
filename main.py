from src.process import Process

process = Process()

for i in range(0, 100):
    print(f'Starting year number {i + 1} without process')
    print(f'Current population is {len(process.inland.inland_population.individuals)}')
    print(f'Current iq distribution is {process.inland.current_iq_distribution}')
    # print(f'Current average age is {process.inland.current_iq_distribution}')
    process.skip_process()

process.inland.inland_population.get_current_iq_distribution(draw=True)

for i in range(0, 10000):
    print(f'Year of the process {i + 1}')
    print(f'Current population is {len(process.inland.inland_population.individuals)}')
    print(f'Current iq distribution is {process.inland.current_iq_distribution}')
    process.execute_process()

process.inland.inland_population.get_current_iq_distribution(draw=True)
