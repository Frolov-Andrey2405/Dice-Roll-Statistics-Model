import random
from tqdm import tqdm

print('''
Dice Roll Statistics Model

Enter how many six-sided dice you want to roll:''')
numberOfDice = int(input('> '))

# Set up a dictionary to store the results of each dice roll:
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0

# Simulate dice rolls:
print(f'Simulating 1,000,000 rolls of {numberOfDice} dice...')
with tqdm(total=1000000) as pbar:
    for i in range(1000000):
        total = 0
        for j in range(numberOfDice):
            total = total + random.randint(1, 6)
        results[total] = results[total] + 1
        pbar.update(1)

# Display results:
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print(f'  {i} - {roll} rolls - {percentage}%')
