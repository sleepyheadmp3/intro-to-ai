import sys, parse, grader
from heapq import heappush, heappop

def greedy_search(problem):
    # frontier as priority queue with heuristic costs
    start = problem["start"]
    goal = problem["goals"]
    explored = set()
    explored_order = []
    solution_path = []

    frontier = []
    heappush(frontier, (float(problem["heuristics"][start]), [start]))
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
                for child in problem["adj"][node]:
                    heappush(frontier, 
                             (float(problem["heuristics"][child]), 
                              path[1] + [child]))

    solution = " ".join(explored_order) + "\n" + " ".join(solution_path)
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 4
    grader.grade(problem_id, test_case_id, greedy_search, 
                 parse.read_graph_search_problem)