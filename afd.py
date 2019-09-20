def verify_afd(name, final_states, initial_state, delta, string, sigma):
    current_state = initial_state
    print("\n", "AFD: ", name)
    print("Initial state: ", initial_state)

    # For each character of the input:
    for char in string:
        print("Input: ", char)
        if char not in sigma:
            print("Character not present in Alphabet")
            return False
        # Check if there is a function with the current state and the
        # char in delta. I yes, go to the state defined in delta:
        for function in delta:
            if function[0] is current_state and function[1] is char:
                current_state = function[2]
                print("Next state: ", current_state)
                break
        print("Last state: ", current_state)

        # If it stop in a goal state, returns True. Otherwise, False.
    if current_state in final_states:
        return True
    return False