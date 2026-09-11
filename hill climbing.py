def hill_climbing(states, start):
    current = start
    iteration = 1

    print("\n===== Hill Climbing =====")
    print("Starting State:", current)
    print("Starting Value:", states[current]["value"])

    while True:
        print(f"\n--- Iteration {iteration} ---")
        print("Current State:", current)
        print("Current Value:", states[current]["value"])

        neighbors = states[current]["neighbors"]
        print("Neighbors:", neighbors)

        if not neighbors:
            print("No neighbors available.")
            print("Reached a final state.")
            return current

        best_neighbor = max(
            neighbors,
            key=lambda x: states[x]["value"]
        )

        print("Best Neighbor:", best_neighbor)
        print("Best Neighbor Value:", states[best_neighbor]["value"])

        if states[best_neighbor]["value"] <= states[current]["value"]:
            print("Best neighbor is not better than current state.")
            print("Stopping the search.")
            return current

        print(f"Moving from {current} -> {best_neighbor}")

        current = best_neighbor
        iteration += 1


# TEST CASE 1
states = {

    "A": {"value": 1, "neighbors": ["B", "D"]},

    "B": {"value": 5, "neighbors": ["A", "C"]},

    "C": {"value": 3, "neighbors": ["B", "E"]},

    "D": {"value": 2, "neighbors": ["A", "F"]},

    "E": {"value": 4, "neighbors": ["C", "H"]},

    "F": {"value": 6, "neighbors": ["D", "G"]},

    "G": {"value": 10, "neighbors": ["F", "H"]},

    "H": {"value": 5, "neighbors": ["G", "E"]},

}

result = hill_climbing(states, "A")

print("\n===== FINAL RESULT =====")
print("Hill Climbing Result:", result)
print("Value:", states[result]["value"])
