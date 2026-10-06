rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        ch = input("Enter a character: ")
        row.append(ch)
    matrix.append(row)

print(matrix)

target = input("Enter the word you want to search: ")


def find(mat, word):
    if not mat or not mat[0]:
        return False

    rows, cols = len(mat), len(mat[0])

    def dfs(r, c, index, visited):
        if index == len(word):
            return True

        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or (r, c) in visited
            or mat[r][c] != word[index]
        ):
            return False

        visited.add((r, c))

        for dr, dc in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]:
            if dfs(r + dr, c + dc, index + 1, visited):
                return True

        visited.remove((r, c))
        return False

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == word[0]:
                if dfs(i, j, 0, set()):
                    return True

    return False


if find(matrix, target):
    print("Word found!")
else:
    print("Word not found!")