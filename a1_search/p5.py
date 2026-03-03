import sys, parse, grader
from heapq import heappush, heappop

def astar_search(problem):
    # frontier as priority queue with heuristic + backwards costs
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
        g_n = path[0] - problem["heuristics"][node]
        if node in goal:
            solution_path = path[1]
            break
        if node not in explored:
            explored_order.append(node)
            explored.add(node)
            if node in problem["adj"]:
                for child, value in problem["adj"][node].items():
                    heappush(frontier, (
                        float(g_n + value + problem["heuristics"][child]),
                        path[1] + [child]))

    solution = " ".join(explored_order) + "\n" + " ".join(solution_path)
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 5
    grader.grade(problem_id, test_case_id, astar_search,
                 parse.read_graph_search_problem)