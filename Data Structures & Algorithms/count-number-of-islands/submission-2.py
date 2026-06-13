class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        islands = 0

        # def dfs(r, c):
        #     if  r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
        #         return

        #     grid [r][c] = "*"

        #     dfs(r + 1, c)
        #     dfs(r, c + 1)
        #     dfs(r - 1, c)
        #     dfs(r, c - 1)

        directions = [(1, 0), (0 ,1), (-1, 0), (0, -1)]

        def iterative_dfs(r, c):
            stack = [(r, c)]

            while stack:
                i, j = stack.pop()
                grid[i][j] = "*"

                for dr, dc in directions:
                    nr, nc = dr + i, dc + j
                    if  0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        stack.append((nr, nc)) 

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    iterative_dfs(i, j)
        
        return islands