def read_txt(path, mode="r"):
    file = open(path, mode)

    content = file.readlines()

    name = content[0]
    number_of_states = int(content[1].rstrip())
    states = [i for i in range(0, number_of_states)]
    initial_state = content[2].rstrip()
    sigma = content[3].rstrip()
    final_states = content[4].replace('\n', '').split(',')

    delta = []

    for i in range(5, len(content)):
        append_to_delta = content[i].replace('\n', '').split(',')
        delta.append(append_to_delta)

    return name, states, initial_state, sigma, final_states, delta
