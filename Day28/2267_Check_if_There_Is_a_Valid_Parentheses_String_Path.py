# def get_matrix_paths(matrix):
#     m = len(matrix)
#     n = len(matrix[0]) if m > 0 else 0
#     all_paths = []
#
#     def dfs(r, c, current_path):
#         current_path.append(matrix[r][c])
#
#         if r == m - 1 and c == n - 1:
#             all_paths.append("".join(current_path))
#         else:
#             if c + 1 < n:
#                 dfs(r, c + 1, current_path)   # Right
#             if r + 1 < m:
#                 dfs(r + 1, c, current_path)   # Down
#
#         current_path.pop()  # Backtrack
#
#     if m > 0 and n > 0:
#         dfs(0, 0, [])
#
#     return all_paths
#
#
# # Your specific matrix
# matrix = [
#     ["(", "(", "("],
#     [")", "(", ")"],
#     ["(", "(", ")"],
#     ["(", "(", ")"]
# ]
#
# # Run the function and save the list
# saved_paths = get_matrix_paths(matrix)
#
# # Print the results
# print(f"Successfully saved {len(saved_paths)} paths:\n")
# for i, path in enumerate(saved_paths, 1):
#     print(f"Path {i}: {path}")

def hasValidPath(grid: list[list[str]]) -> bool:
    m, n = len(grid), len(grid[0])

    all_paths = []

    def backtrack(row, col, current):
        current.append(grid[row][col])

        if row == m - 1 and col == n - 1:
            all_paths.append("".join(current))

        else:
            if col + 1 < n:
                backtrack(row, col + 1, current)

            if row + 1 < m:
                backtrack(row + 1, col, current)

        current.pop()

    backtrack(0, 0, [])

    for path in all_paths:
        count = 0
        valid = True
        for ch in path:
            if ch == "(":
                count += 1
            if ch == ")":
                count -= 1
            if count < 0:
                valid = False
                break
        if valid and count == 0:
            return True

    return False

matrix = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]

print(hasValidPath(matrix))