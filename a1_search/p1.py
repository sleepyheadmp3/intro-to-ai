import sys, grader, parse
from collections import deque

def dfs_search(problem):
    # frontier deque of nested lists acts as a LIFO stack
    start = problem["start"]
    goal = problem["goals"]
    frontier = deque([[start]])
    explored = set()
    explored_order = []
    solution_path = []

    while frontier:
        path = frontier.pop()
        node = str(path[-1])
        if node in goal:
            solution_path = path
            break
        if node not in explored:
            explored_order.append(node)
            explored.add(node)
            if node in problem["adj"]:
                for child in problem["adj"][node]:
                    frontier.append(path + [child])

    solution = " ".join(explored_order) + "\n" + " ".join(solution_path)
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 1
    grader.grade(problem_id, test_case_id, dfs_search, 
                 parse.read_graph_search_problem)
