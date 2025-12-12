import time
from copy import deepcopy

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
            distance = r - row
            conflicts = {col, col - distance, col + distance}
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

    start_time = time.time()
    solve(0, domains)
    end_time = time.time()

    return solutions, recursive_calls, prune_count, end_time - start_time

# -------- MAIN --------
if __name__ == "__main__":
    N = int(input("Enter value of N for N-Queens (Forward Checking): "))

    solutions, calls, prunes, exec_time = solve_nqueens_forward_checking(N)

    print("\n--- Forward Checking Result ---")
    print(f"N = {N}")
    print(f"Number of solutions: {len(solutions)}")
    print(f"Recursive calls: {calls}")
    print(f"Pruned domain values: {prunes}")
    print(f"Execution time: {exec_time:.6f} seconds")

    if len(solutions) == 0:
        print("No solution exists.")
    elif N <= 5:
        print("\nSolutions (row -> column index):")
        for sol in solutions:
            print(sol)
