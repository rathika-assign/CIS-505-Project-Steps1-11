# nqueen_backtracking.py
# Backtracking solution for N-Queens with user input

import time

def solve_nqueens_backtracking(N):
    board = [-1] * N
    solutions = []
    recursive_calls = 0

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == row - r:
                return False
        return True

    def solve(row):
        nonlocal recursive_calls
        recursive_calls += 1
        if row == N:
            solutions.append(board.copy())
            return
        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    start_time = time.time()
    solve(0)
    end_time = time.time()

    return solutions, recursive_calls, end_time - start_time

# -------- MAIN --------
if __name__ == "__main__":
    N = int(input("Enter value of N for N-Queens (Backtracking): "))

    solutions, calls, exec_time = solve_nqueens_backtracking(N)

    print("\n--- Backtracking Result ---")
    print(f"N = {N}")
    print(f"Number of solutions: {len(solutions)}")
    print(f"Recursive calls: {calls}")
    print(f"Execution time: {exec_time:.6f} seconds")

    if len(solutions) == 0:
        print("No solution exists.")
    elif N <= 5:
        print("\nSolutions (row -> column index):")
        for sol in solutions:
            print(sol)
