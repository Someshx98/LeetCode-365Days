def solveNQueens(n: int):
    results = []

    # Track occupied columns and diagonals
    # main_diag = (row - col), anti_diag = (row + col)
    cols = set()
    main_diag = set()
    anti_diag = set()

    # Board representation: board[r] stores the column index of the queen in row r
    board = []

    def backtrack(row):
        # Base case: All queens successfully placed
        if row == n:
            # Construct formatted string board
            solution = []
            for c in board:
                solution.append("." * c + "Q" + "." * (n - c - 1))
            results.append(solution)
            return

        for col in range(n):
            if col in cols or (row - col) in main_diag or (row + col) in anti_diag:
                continue  # Under attack, try next column

            # Place queen
            cols.add(col)
            main_diag.add(row - col)
            anti_diag.add(row + col)
            board.append(col)

            # Recurse to next row
            backtrack(row + 1)

            # Backtrack (undo move)
            cols.remove(col)
            main_diag.remove(row - col)
            anti_diag.remove(row + col)
            board.pop()

    backtrack(0)
    return results


# Example Usage:
n = int(input("Enter the size of the board: "))
solutions = solveNQueens(n)

print(f"Total solutions for N={n}: {len(solutions)}\n")
for sol in solutions:
    for row in sol:
        print(row)
    print()