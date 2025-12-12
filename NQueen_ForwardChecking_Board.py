# nqueen_forward_checking.py
import time
from copy import deepcopy

def print_board(solution):
    N = len(solution)
    for row in range(N):
        for col in range(N):
            print("Q" if solution[row] == col else ".", end=" ")
        print()
    print()

def solve_nqueens_forward_checking(N):
    board = [-1] * N
    solutions = []
    recursive_calls = 0
    prune_count = 0

    domains = [list(range(N)) for _ in range(N)]

    def forward_check(domains, row, col):
        nonlocal prune_count
        new_domains = deepcopy(domains)
        for r in range(row + 1, N):
            diff = r - row
            conflicts = {col, col - diff, col + diff}
            for c in conflicts:
                if c in new_domains[r]:
                    new_domains[r].remove(c)
                    prune_count += 1
            if not new_domains[r]:
                return None
        return new_domains

    def solve(row, domains):
        nonlocal recursive_calls
        recursive_calls += 1
        if row == N:
            solutions.append(board.copy())
            return
        for col in domains[row]:
            board[row] = col
            new_domains = forward_check(domains, row, col)
            if new_domains is not None:
                solve(row + 1, new_domains)
            board[row] = -1

    start = time.time()
    solve(0, domains)
    end = time.time()

    return solutions, recursive_calls, prune_count, end - start

# -------- MAIN --------
if __name__ == "__main__":
    N = int(input("Enter value of N (Forward Checking): "))

    solutions, calls, prunes, exec_time = solve_nqueens_forward_checking(N)

    print("\n--- Forward Checking Result ---")
    print(f"N = {N}")
    print(f"Total Solutions: {len(solutions)}")
    print(f"Recursive Calls: {calls}")
    print(f"Pruned Values: {prunes}")
    print(f"Execution Time: {exec_time:.6f} seconds")

    if len(solutions) == 0:
        print("No solution exists.")
    else:
        print("\nDisplaying first 2 solutions:\n")
        for i, sol in enumerate(solutions[:2], 1):
            print(f"Solution {i}:")
            print_board(sol)
