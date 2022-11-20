def parse_file(file_name):
    f = open(file_name, "r")
    lines = f.readlines()
    return lines[0]


def SolveGame(method_name, problem_file_name, player_type):
    state = parse_file(problem_file_name)
    print(state)

    if method_name == "Minimax":
        return minimax_nim(state)
    elif method_name == "AlphaBeta":
        return minimax_alphabeta(state)
    else:
        print("Error: unexpected method name")
    return


def minimax_nim(state):
    res = minimax_nim_impl(state, True, 0, [])
    # todo: do something with result
    return


def minimax_nim_impl(state, is_max, iteration, list_until):
    # I think I can implement this.
    # Then go to bed.
    # It's 22.40. Give me an hour for this.
    # Let's make a coffee?x

    iteration = iteration + 1
    list_until.append(state)

    if state == (0, 0, 0):
        if is_max:
            return 1, iteration, list_until
        else:
            return -1, iteration, list_until

    if is_max:
        # todo: handle max case
        return
    else:
        # todo: handle min case
        return

    print("error: reached unexpected code")
    return -1


def get_children(state):
    res = []
    ox, oy, oz = state

    for x in range(ox):
        res.append((x, oy, oz))

    for y in range(oy):
        res.append((ox, y, oz))

    for z in range(oz):
        res.append((ox, oy, z))

    return res


def minimax_alphabeta(state):
    return


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # SolveGame("Minimax", "nim1.txt", "MAX")
    print(get_children([1, 3, 5]))
