class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        k = 1024
    
        previous = [[False] * k for _ in range(col)]
    
        for i in range(row):
            current = [[False] * k for _ in range(col)]
            for j in range(col):
                x = grid[i][j]
                if i == 0 and j == 0:
                    current[0][x] = True
                    continue
    
                for t in range(k):
                    if (i > 0 and previous[j][t]) or (j > 0 and current[j - 1][t]):
                        current[j][t ^ x] = True
    
            previous = current
    
        return min(s for s in range(k) if previous[col - 1][s])