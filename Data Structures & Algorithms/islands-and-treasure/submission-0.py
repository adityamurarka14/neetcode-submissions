class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0,1], [-1, 0], [0, -1]]
        gatesQueue = deque()
        distance = 1
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    gatesQueue.append((x,y))

        while gatesQueue:
            currR, currC = gatesQueue.popleft()
            for a,b in directions:
                r, c = a + currR, b + currC
                if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] and grid[r][c] == 2147483647:
                    grid[r][c] = grid[currR][currC] + 1
                    gatesQueue.append((r,c))

        print(gatesQueue, grid)