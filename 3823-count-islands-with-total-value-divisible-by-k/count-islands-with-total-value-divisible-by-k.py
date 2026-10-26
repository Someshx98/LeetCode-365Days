class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        row, col = len(grid), len(grid[0])
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        visited = [[False] * col for _ in range(row)]
        result = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0 and not visited[i][j]:
                    total = 0
                    visited[i][j] = True
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        total += grid[x][y]
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if(0 <= nx < row and 0 <= ny < col and grid[nx][ny] > 0 and not visited[nx][ny]):
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                    if total % k == 0:
                       result += 1

        return result