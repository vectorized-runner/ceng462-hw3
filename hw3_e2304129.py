def parse_file(file_name):
    f = open(file_name, "r")
    lines = f.readlines()
    line = eval(lines[0])
    return tuple(line)


def SolveGame(method_name, problem_file_name, player_type):
    state = parse_file(problem_file_name)
    is_max = player_type == "MAX"

    print(f"state: {state}")

    if method_name == "Minimax":
        return minimax_nim(state, is_max)
    elif method_name == "AlphaBeta":
        return minimax_alphabeta(state, is_max)
    else:
        print("Error: unexpected method name")
    return


def minimax_nim(state, is_max):
    utility, iterations, search = minimax_nim_impl(state, is_max, 0, [])

    # Correct action is the search[0]
    correct_action = search[0]
    # Run algorithm with correct action to find the iterations for that path
    _, iterations, _ = minimax_nim_impl(correct_action, not is_max, 0, [])

    return [correct_action, iterations - 1]


def minimax_nim_impl(state, is_max, iterations, path):
    iterations = iterations + 1
    path.append(state)

    if state == (0, 0, 0):
        if is_max:
            return 1, iterations, path
        else:
            return -1, iterations, path

    if is_max:
        children = get_children(state)
        max_utility = -10000
        max_path = None
        child_is_max = not is_max

        for child in children:
            utility, child_iter, child_path = minimax_nim_impl(child, child_is_max, 0, [])
            iterations += child_iter
            if utility > max_utility:
                max_path = child_path
                max_utility = utility

        path.extend(max_path)

        return max_utility, iterations, max_path
    else:
        children = get_children(state)
        min_utility = 10000
        min_path = None
        child_is_max = not is_max

        for child in children:
            child_util, child_iter, child_path = minimax_nim_impl(child, child_is_max, 0, [])
            iterations += child_iter
            if child_util < min_utility:
                min_path = child_path
                min_utility = child_util

        path.extend(min_path)

        return min_utility, iterations, path

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
    res = minimax_nim((1, 3, 5), True)
    print(res)
# print(res)
