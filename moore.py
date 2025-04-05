import json

# Input JSON 
data = {
    "states": {
        "q0": "A", "q1": "B", "q2": "C", "q3": "D", "q4": "E"
    },
    "transitions": {
        "q0": {"0": "q1", "1": "q2"},
        "q1": {"0": "q3", "1": "q4"},
        "q2": {"0": "q4", "1": "q0"},
        "q3": {"0": "q0", "1": "q2"},
        "q4": {"0": "q2", "1": "q1"}
    },
    "initial_state": "q0",
    "test_string": "011010110"
}

def moore_machine_simulator(data):
    states = data["states"]
    transitions = data["transitions"]
    current_state = data["initial_state"]
    test_string = data["test_string"]

    path = [current_state]
    output = [states[current_state]]

    for symbol in test_string:
        current_state = transitions[current_state][symbol]
        path.append(current_state)
        output.append(states[current_state])

    return path, output

# Jalankan simulasi
path, output = moore_machine_simulator(data)

# Format hasil
print("Path: " + " → ".join(path))
print("Output: " + "".join(output))
