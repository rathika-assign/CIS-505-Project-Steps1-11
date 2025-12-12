from time import perf_counter
from copy import deepcopy

def backtracking_nqueens(N, max_show=5):
    """Classic DFS backtracking: board[row] = column"""
    board = [-1] * N
    solutions = []
    rec_calls = 0
    conflict_checks = 0

    def is_safe(row, col):
        nonlocal conflict_checks
        conflict_checks += 1
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == row - r:
                return False
        return True

    def solve(row):
        nonlocal rec_calls
        rec_calls += 1
        if row == N:
            solutions.append(board.copy())
            return
        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    t0 = perf_counter()
    solve(0)
    t1 = perf_counter()
    return {
        "algorithm": "Backtracking",
        "N": N,
        "solutions_count": len(solutions),
        "solutions_preview": solutions[:max_show],
        "recursive_calls": rec_calls,
        "conflict_checks": conflict_checks,
        "time_s": t1 - t0
    }

def forward_checking_nqueens(N, max_show=5):
    """Forward checking with domains stored per row (deepcopied on assignment)."""
    board = [-1] * N
    solutions = []
    rec_calls = 0
    prune_count = 0  # count of domain entries removed
    conflict_checks = 0  # approximate (counts membership checks)

    def remove_conflicts(domains, row, col):
        nonlocal prune_count, conflict_checks
        new_domains = deepcopy(domains)
        removed = 0
        for r in range(row+1, N):
            # remove same column
            if col in new_domains[r]:
                new_domains[r].remove(col)
                removed += 1
            # diagonal left
            d_left = col - (r - row)
            if d_left in new_domains[r]:
                new_domains[r].remove(d_left)
                removed += 1
            # diagonal right
            d_right = col + (r - row)
            if d_right in new_domains[r]:
                new_domains[r].remove(d_right)
                removed += 1
            # approximate conflict checks
            conflict_checks += 3
            if len(new_domains[r]) == 0:
                prune_count += removed
                return None, removed
        prune_count += removed
        return new_domains, removed

    def solve(row, domains):
        nonlocal rec_calls
        rec_calls += 1
        if row == N:
            solutions.append(board.copy())
            return
        # iterate over a static copy of domains[row]
        for col in domains[row][:]:
            board[row] = col
            new_domains, removed = remove_conflicts(domains, row, col)
            if new_domains is not None:
                solve(row + 1, new_domains)
            board[row] = -1

    domains0 = [list(range(N)) for _ in range(N)]
    t0 = perf_counter()
    solve(0, domains0)
    t1 = perf_counter()
    return {
        "algorithm": "Forward-Checking",
        "N": N,
        "solutions_count": len(solutions),
        "solutions_preview": solutions[:max_show],
        "recursive_calls": rec_calls,
        "prune_count": prune_count,
        "conflict_checks_est": conflict_checks,
        "time_s": t1 - t0
    }

if __name__ == "__main__":
    test_cases = [1, 4, 8, 10]  # TC1, TC2, TC3, optional TC4 from your plan
    results = []
    for N in test_cases:
        bt = backtracking_nqueens(N)
        fc = forward_checking_nqueens(N)
        results.append((bt, fc))

    # Print a terminal-like run summary (screen prints)
    print("=== N-Queens Algorithm Comparison ===")
    for bt_res, fc_res in results:
        print(f"\n--- N = {bt_res['N']} ---")
        print(f"[Backtracking] Solutions: {bt_res['solutions_count']}, RecCalls: {bt_res['recursive_calls']}, "
            f"ConflictChecks: {bt_res['conflict_checks']}, Time(s): {bt_res['time_s']:.6f}")
        if bt_res['solutions_count'] <= 10:
            for sol in bt_res['solutions_preview']:
                print("  Solution:", sol)
        print(f"[Forward-Checking] Solutions: {fc_res['solutions_count']}, RecCalls: {fc_res['recursive_calls']}, "
            f"PruneOps: {fc_res['prune_count']}, ConflictChecks(est): {fc_res['conflict_checks_est']}, "
            f"Time(s): {fc_res['time_s']:.6f}")
        if fc_res['solutions_count'] <= 10:
            for sol in fc_res['solutions_preview']:
                print("  Solution:", sol)

    # compact comparison
    print("\n=== Summary Table ===")
    print(f"{'N':>3} | {'Alg':^18} | {'Solutions':>9} | {'RecCalls':>9} | {'PruneOps':>9} | {'Time(s)':>8}")
    print("-"*70)
    for bt_res, fc_res in results:
        print(f"{bt_res['N']:>3} | {'Backtracking':^18} | {bt_res['solutions_count']:>9} | {bt_res['recursive_calls']:>9} | {'-':>9} | {bt_res['time_s']:>8.6f}")
        print(f"{fc_res['N']:>3} | {'Forward-Checking':^18} | {fc_res['solutions_count']:>9} | {fc_res['recursive_calls']:>9} | {fc_res['prune_count']:>9} | {fc_res['time_s']:>8.6f}")
        print("-"*70)

    print("\nRun complete.")
