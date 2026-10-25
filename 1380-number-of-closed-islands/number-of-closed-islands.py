class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        count = 0
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row -1 or j == 0 or j == col - 1:
                    continue
        
                if grid[i][j] == 0:
                    closed = True
                    stack = [(i, j)]
                    grid[i][j] == 1
        
                    while stack:
                        x, y = stack.pop()
        
                        if x == 0 or x == row - 1 or y == 0 or y == col - 1:
                            closed = False
        
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0:
                                grid[nx][ny] = 1
                                stack.append((nx, ny))
        
                    if closed:
                        count += 1
        
        return count