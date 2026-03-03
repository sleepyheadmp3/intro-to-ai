import sys, parse, grader
from p6 import get_result_list

def better_board(problem):
    # get queen coordinates
    board = problem["board"]
    q_rows = problem["queen_rows"]
    queens = []
    for i in range(8):
        queens.append([q_rows[i], i])

    attacks = get_result_list(problem)
    mininum = min([min(row) for row in attacks])
    for i in range(8):
        for j in range(8):
            if int(attacks[i][j]) == mininum:
                for q in queens:
                    if q[1] == j:
                        board[q[0]][j] = "."
                        board[i][j] = "q"
                        solution = "\n".join(
                            [" ".join(line) for line in board])
                        return solution
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 7
    grader.grade(problem_id, test_case_id, better_board, parse.read_8queens_search_problem)