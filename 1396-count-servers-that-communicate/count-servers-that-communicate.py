class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        row_count = [0] * rows
        col_count = [0] * cols

        i = 0

        while i < rows:
            j = 0
            while j < cols:
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

                j += 1
            i += 1

        i = 0
        while i < rows:
            j = 0
            while j < cols:
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1

                j += 1
            i += 1

        return count