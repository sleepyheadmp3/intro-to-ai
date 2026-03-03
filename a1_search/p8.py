# referenced geeksforgeeks on a/b pruning and minimax algorithm
import sys, parse, grader

INF = float("inf")

def adversarial_search(problem):
    root = problem["root"]
    node_type = problem["node_type"]
    utility = problem["utility"]
    edges = problem["edges"]

    # return early if root is only node
    if node_type.get(root) == "LEAF":
        value = str(utility[root])
        return "minimax: None " + value + '\n' + \
                "alphabeta: None " + value + '\n' + \
                "minimax_leaves: " + root + '\n' + \
                "alphabeta_leaves: " + root
    
    mm_leaves = []
    mm_value = 0
    mm_action = ""

    ab_leaves = []
    ab_action = ""
    a = -INF    # alpha = max
    b = INF     # beta = min

    def minimax(node):
        if node_type.get(node) == "LEAF":
            mm_leaves.append(node)
            return utility[node]

        children = edges.get(node, [])

        if node_type.get(node) == "MAX":
            value = -INF
            for x, child in children:
                child_value = minimax(child)
                if child_value > value:
                    value = child_value
            return value

        value = INF
        for x, child in children:
            child_value = minimax(child)
            if child_value < value:
                value = child_value
        return value

    def ab_value(node, alpha, beta):
        if node_type.get(node) == "LEAF":
            ab_leaves.append(node)
            return utility[node]

        children = edges.get(node, [])
        if node_type.get(node) == "MAX":
            value = -INF

            for x, child in children:
                child_value = ab_value(child, alpha, beta)
                if child_value > value:
                    value = child_value
                if value >= beta:
                    # ignore rest
                    break
                if value > alpha:
                    alpha = value
            return value

        value = INF
        for x, child in children:
            child_value = ab_value(child, alpha, beta)
            if child_value < value:
                value = child_value
            if value <= alpha:
                break
            if value < beta:
                beta = value
        return value
    
    if node_type.get(root) == "MAX":
        mm_value = -INF
    else:
        mm_value = INF

    # computes minimax for layer below root
    r_children = edges.get(root, [])

    for action, child in r_children:
        child_value = minimax(child)
        if node_type.get(root) == "MAX":
            if child_value > mm_value:
                mm_value = child_value
                mm_action = action
        else:
            if child_value < mm_value:
                mm_value = child_value
                mm_action = action

    # use a/b pruning on the rest of hte tree
    if node_type.get(root) == "MAX":
        ab_result = -INF
    else:
        ab_result = INF

    for action, child in r_children:
        child_value = ab_value(child, a, b)

        if node_type.get(root) == "MAX":
            # update ideal actions and max
            if child_value > ab_result:
                ab_result = child_value
                ab_action = action

            if child_value > a:
                a = child_value
        else:
            # update ideal actions for min
            if child_value < ab_result:
                ab_result = child_value
                ab_action = action
            if child_value < b:
                b = child_value

    min_leaves_str = " ".join(mm_leaves)
    ab_leaves_str = " ".join(ab_leaves)

    return "minimax: " + mm_action + " " + str(int(mm_value)) + '\n' + \
                "alphabeta: " + ab_action + " " + str(int(ab_result)) + '\n' + \
                "minimax_leaves: " + min_leaves_str + '\n' + \
                "alphabeta_leaves: " + ab_leaves_str 
    

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 8
    grader.grade(problem_id, test_case_id, adversarial_search, parse.read_game_tree_problem)