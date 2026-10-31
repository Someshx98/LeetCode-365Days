class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        f = [[[0, 0] for _ in range(col)] for _ in range(row)]
        f[0][0][0] = 1

        for i in range(row):
            for j in range(col):
                r, d = f[i][j]
                if r == 0 and d == 0:
                    continue

                if grid[i][j] == 0:
                    t = (r + d) % mod
                    if j + 1 < col:
                        f[i][j + 1][0] = (f[i][j + 1][0] + t) % mod
                    if i + 1 < row:
                        f[i + 1][j][1] = (f[i + 1][j][1] + t) % mod
                else:
                    if i + 1 < row:
                        f[i + 1][j][1] = (f[i + 1][j][1] + r) % mod
                    if j + 1 < col:
                        f[i][j + 1][0] = (f[i][j + 1][0] + d) % mod

        return (f[row - 1][col - 1][0] + f[row - 1][col - 1][1]) % mod