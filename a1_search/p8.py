import sys, parse, grader

INF = float("inf")

def adversarial_search(problem):
    return "1"

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 8
    grader.grade(problem_id, test_case_id, adversarial_search, parse.read_game_tree_problem)