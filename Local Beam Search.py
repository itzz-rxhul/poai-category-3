'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def local_beam_search(states, initial_states, k=2):

    current_states = initial_states

    while True:

        successors = []

        for state in current_states:
            successors.extend(states[state]["neighbors"])

        if not successors:
            return max(
                current_states,
                key=lambda x: states[x]["value"]
            )

        # Remove duplicates
        successors = list(set(successors))

        # Select best K states
        best_states = sorted(
            successors,
            key=lambda x: states[x]["value"],
            reverse=True
        )[:k]

        # Stop if no improvement
        if all(
            states[s]["value"] <=
            max(states[c]["value"] for c in current_states)
            for s in best_states
        ):
            return max(
                current_states,
                key=lambda x: states[x]["value"]
            )

        current_states = best_states


result = local_beam_search(
    states,
    ["B", "C"],
    k=2
)

print("Local Beam Search Result:", result)
print("Value:", states[result]["value"])