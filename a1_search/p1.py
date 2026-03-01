import sys, grader, parse

def dfs_search(problem):
    #Your p1 code here
    # fringe is LIFO stack
    # tree search but track visited
    # store closed set as a set

    # closed = empty set
    # fringe = insert(make-node(initial-state[problem]), fringe)
    # loop do:
        # if fringe is empty, then return failure
        # node = pop front(fringe)
        # if goal-test(problem, state[node]), then return node
        # if state[node] is not in closed, then:
            # add state[node] to closed
            # for child-node in expand(state[node], problem), do
                # fringe = insert(child-node, fringe)


    solution = 'Ar D C\nAr C G'
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 1
    grader.grade(problem_id, test_case_id, dfs_search, parse.read_graph_search_problem)