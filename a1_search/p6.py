import sys, parse, grader

def number_of_attacks(problem):
    board = problem["board"]
    q_rows = problem["queen_rows"]

    n = len(board)
    queens = []
    result_rows = []

    # get queen coordinates
    for i in range(8):
        queens.append([q_rows[i], i])
        
    for i in range(n):      # row
        row_result = []
        for j in range(n):      # col
            moved = []
            for q in queens:
                if q[1] != j:
                    moved.append(q)
            moved.append([i, j])

            attacks = 0
            for q1 in range(n):
                for q2 in range(q1 + 1, n):
                    queen1 = moved[q1]
                    queen2 = moved[q2]
                    # same row or diagonal
                    if queen1[0] == queen2[0] or \
                        abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
                        attacks += 1
            
            # adds space if single digit
            if attacks < 10:
                row_result.append(" " + str(attacks))
            else:
                row_result.append(str(attacks))
        result_rows.append(" ".join(row_result))

    solution = "\n".join(result_rows)
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 6
    grader.grade(problem_id, test_case_id, number_of_attacks, 
                 parse.read_8queens_search_problem)