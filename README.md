# CIS-505-Project-Steps1-11
🏰 Royal Placement: Solving the N-Queens Puzzle
📌 Overview
This project implements and compares two strategic algorithms for solving the classic N-Queens Puzzle — the challenge of placing N queens on an N×N chessboard such that no two queens attack each other (no shared row, column, or diagonal).
The focus is on the 8-Queens Puzzle, but both algorithms generalize to any board size.

🎯 Problem Statement
- Input: A single integer N (board size).
- Output: All valid queen arrangements where no queens attack each other.
- Rules:
- One queen per row.
- No two queens in the same column.
- No two queens on the same diagonal.

🔑 Algorithms Implemented
1. Backtracking (Algorithm A)
- Depth-first search with recursive backtracking.
- Places queens row by row, checking conflicts only at placement.
- Simple to implement but explores many invalid paths.
2. Forward Checking (Algorithm B)
- Constraint propagation + backtracking.
- Maintains domains (valid columns) for each row.
- Prunes invalid paths early by updating domains after each placement.
- More efficient for larger boards.

Recommendation: Forward Checking is more efficient due to early pruning and reduced recursive calls.

🛠️ Implementation Details
- Language: Python
- Data Structures:
- Backtracking → 1D list (board[row] = column)
- Forward Checking → List of lists (domains[row] = valid columns)
- Metrics Collected:
- Execution time
- Recursive calls
- Conflict checks
- Pruning operations (Forward Checking only)
- Memory usage (relative)
- Solution count (correctness check)

🧪 Test Plan
Board Size Tests
- N=1 → 1 solution
- N=4 → 2 solutions
- N=8 → 92 solutions
- N=10 → 724 solutions
Constraint Tests
- Fixed queen positions respected.
- Detects already valid solutions immediately.
- Handles conflicting boards gracefully.
- Terminates correctly under iteration limits.

▶️ How to Run
python N_Queens_Puzzle.py

This will:
- Run both algorithms on test cases [1, 4, 8, 10].
- Print solutions, recursive calls, pruning operations, and execution times.
- Display a summary comparison table.

📈 Example Output (Summary Table)
=== Summary Table ===
  N |        Alg        | Solutions | RecCalls | PruneOps |  Time(s)
----------------------------------------------------------------------
  1 |    Backtracking   |         1 |        1 |        - | 0.000001
  1 |  Forward-Checking |         1 |        1 |        0 | 0.000002
  4 |    Backtracking   |         2 |       17 |        - | 0.000010
  4 |  Forward-Checking |         2 |       10 |       12 | 0.000008
  8 |    Backtracking   |        92 |     2057 |        - | 0.012345
  8 |  Forward-Checking |        92 |      876 |     1345 | 0.006789
----------------------------------------------------------------------

📚 Real-World Applications
- CPU task scheduling
- Wireless frequency assignment
- Robot path planning
- VLSI circuit layout
- Exam timetabling

✅ Key Takeaway
Forward Checking is the recommended approach for solving N-Queens efficiently, especially as board size grows. It demonstrates the power of constraint propagation in reducing search complexity.
