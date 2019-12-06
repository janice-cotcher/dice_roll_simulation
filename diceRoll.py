# demonstration of experimental probability with the rol of a single die
# adapted from https://www.pythonforbeginners.com/code-snippets-source-code/game-rolling-the-dice/
import random

# roll a die n_max times and store the rolls in a list
min = 1
max = 6
n = 0
rolls = []
while True:
    max_n = int(input("How many times do you want to roll the die? "))
    try:
        while n <= max_n:
            x = random.randint(min, max)
            rolls.append(x)
            n += 1
        break
    except ValueError:
        print("Invalid choice, try again.")

# count the number of times each number appears in n_max rolls append
# and calculate the percent
for y in range(1, 7):
    print(f"The number of times {y+1} was rolled: {rolls.count(y)}")
    percent = rolls.count(y) * 100 / max_n
    print(f"The percent of times {y+1} was rolled: {percent}")
    print("\n")
