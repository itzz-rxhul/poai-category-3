'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def hill_climbing(states, start):
    current = start

    while True:
        neighbors = states[current]["neighbors"]

        if not neighbors:
            return current

        best_neighbor = max(
            neighbors,
            key=lambda x: states[x]["value"]
        )

        if states[best_neighbor]["value"] <= states[current]["value"]:
            return current

        current = best_neighbor


# State Space
states = {
    "A": {"value": 2, "neighbors": ["B", "C"]},
    "B": {"value": 5, "neighbors": ["A", "D"]},
    "C": {"value": 4, "neighbors": ["A", "E"]},
    "D": {"value": 7, "neighbors": ["B", "F"]},
    "E": {"value": 6, "neighbors": ["C", "G"]},
    "F": {"value": 8, "neighbors": ["D"]},
    "G": {"value": 10, "neighbors": ["E"]},
}

result = hill_climbing(states, "A")

print("Hill Climbing Result:", result)
print("Value:", states[result]["value"])