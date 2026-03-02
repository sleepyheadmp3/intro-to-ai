import sys, parse, grader
from heapq import heappush, heappop
def ucs_search(problem):
    # frontier as priority queue
    start = problem["start"]
    goal = problem["goals"]
    explored = set()
    explored_order = []
    solution_path = []

    frontier = []
    heappush(frontier, (0, [start]))
    while frontier:
        path = heappop(frontier)
        node = str(path[1][-1])
        if node in goal:
            solution_path = path[1]
            break
        if node not in explored:
            explored_order.append(node)
            explored.add(node)
            if node in problem["adj"]:
                for child, value in problem["adj"][node].items():
                    heappush(frontier, 
                             (float(path[0] + value), path[1] + [child]))

    solution = " ".join(explored_order) + "\n" + " ".join(solution_path)
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 3
    grader.grade(problem_id, test_case_id, ucs_search, parse.read_graph_search_problem)