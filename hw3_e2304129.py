def parse_file(file_name):
    return -1


def SolveGame(method_name, problem_file_name, player_type):
    state = parse_file(problem_file_name)

    if method_name == "Minimax":
        minimax_nim(state)
    elif method_name == "AlphaBeta":
        minimax_alphabeta(state)
    else:
        print("Error: unexpected method name")
    return


def minimax_nim(state):
    return


def minimax_alphabeta(state):
    return


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
