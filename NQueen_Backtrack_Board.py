# nqueen_backtracking.py
import time

def print_board(solution):
    N = len(solution)
    for row in range(N):
        for col in range(N):
            print("Q" if solution[row] == col else ".", end=" ")
        print()
    print()

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

    start = time.time()
    solve(0)
    end = time.time()

    return solutions, recursive_calls, end - start

# -------- MAIN --------
if __name__ == "__main__":
    N = int(input("Enter value of N (Backtracking): "))

    solutions, calls, exec_time = solve_nqueens_backtracking(N)

    print("\n--- Backtracking Result ---")
    print(f"N = {N}")
    print(f"Total Solutions: {len(solutions)}")
    print(f"Recursive Calls: {calls}")
    print(f"Execution Time: {exec_time:.6f} seconds")

    if len(solutions) == 0:
        print("No solution exists.")
    else:
        print("\nDisplaying first 2 solutions:\n")
        for i, sol in enumerate(solutions[:2], 1):
            print(f"Solution {i}:")
            print_board(sol)
