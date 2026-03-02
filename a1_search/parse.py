import os, sys
def read_graph_search_problem(file_path):
    start = None
    goals = None
    heuristics = {}
    adj = {}

    with open(file_path, 'r') as f:
        start = f.readline().strip().split()[1]
        goals = f.readline().strip().split()[1:]

        line = f.readline()
        while line:
            line = line.split()
            if len(line) == 2:
                heuristics[line[0]] = int(line[1])
            elif len(line) == 3:
                if line[0] not in adj:
                    adj[line[0]] = {}
                adj[line[0]][line[1]] = float(line[2])
            line = f.readline()

    return {
        "start": start,
        "goals": goals,
        "heuristics": heuristics,
        "adj": adj,
    }

def read_8queens_search_problem(file_path):
    #Your p6 code here
    board = None
    queen_rows = None

    # If some columns are missing queens, keep -1 (shouldn't happen in provided tests)
    return {
        "board": board,
        "queen_rows": queen_rows,
    }


def read_game_tree_problem(filename):
    "your p8 code here"
    root = None
    node_type = None
    utility = None
    edges = None
    return {
        "root": root,
        "node_type": node_type,
        "utility": utility,
        "edges": edges,
    }

if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, test_case_id = sys.argv[1], sys.argv[2]
        if int(problem_id) <= 5:
            problem = read_graph_search_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        elif int(problem_id) <= 7:
            problem = read_8queens_search_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        else:
            problem = read_game_tree_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        print(problem)
    else:
        print('Error: I need exactly 2 arguments!')