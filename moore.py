import json

def simulate_dfa(dfa):
    states = dfa["states"]
    alphabet = dfa["alphabet"]
    start_state = dfa["start_state"]
    accept_states = set(dfa["accept_states"])
    transitions = dfa["transitions"]
    test_string = dfa["test_string"]
    
    current_state = start_state
    path = [current_state]
    
    for symbol in test_string:
        if symbol not in alphabet:
            return "Error: Invalid symbol in input string"
        current_state = transitions[current_state].get(symbol)
        if current_state is None:
            return "Error: No valid transition"
        path.append(current_state)
    
    path_str = " → ".join(path)
    status = "ACCEPTED" if current_state in accept_states else "REJECTED"
    
    return f"Path: {path_str}\nStatus: {status}"

# Contoh penggunaan
dfa_json = '''{
"states": ["q0", "q1", "q2", "q3"],
"alphabet": ["a", "b"],
"start_state": "q0",
"accept_states": ["q2", "q3"],
"transitions": {
"q0": { "a": "q1", "b": "q3" },
"q1": { "a": "q1", "b": "q2" },
"q2": { "a": "q1", "b": "q3" },
"q3": { "a": "q2", "b": "q3" }
},
"test_string": "aaabba"
}'''

dfa = json.loads(dfa_json)
result = simulate_dfa(dfa)
print(result)
