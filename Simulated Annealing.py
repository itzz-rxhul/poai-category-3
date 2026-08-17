'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random
import math


def simulated_annealing(states, start, temperature=100, cooling_rate=0.95):

    current = start
    best = current

    while temperature > 0.1:

        neighbors = states[current]["neighbors"]

        if not neighbors:
            break

        next_state = random.choice(neighbors)

        current_value = states[current]["value"]
        next_value = states[next_state]["value"]

        delta = next_value - current_value

        if delta > 0:
            current = next_state

        else:
            probability = math.exp(delta / temperature)

            if random.random() < probability:
                current = next_state

        if states[current]["value"] > states[best]["value"]:
            best = current

        temperature *= cooling_rate

    return best


result = simulated_annealing(states, "A")

print("Simulated Annealing Result:", result)
print("Value:", states[result]["value"])